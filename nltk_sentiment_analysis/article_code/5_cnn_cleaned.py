import html

import matplotlib.pyplot as plt
import numpy
import preprocessor as tweet_preprocessor
from keras import Sequential, layers
from keras.preprocessing.sequence import pad_sequences
from keras_preprocessing.text import Tokenizer
from nltk import ClassifierI
from nltk.corpus import twitter_samples
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

plt.style.use('ggplot')


def plot_history(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    x = range(1, len(acc) + 1)

    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    plt.plot(x, acc, 'b', label='Training acc')
    plt.plot(x, val_acc, 'r', label='Validation acc')
    plt.title('Training and validation accuracy')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(x, loss, 'b', label='Training loss')
    plt.plot(x, val_loss, 'r', label='Validation loss')
    plt.title('Training and validation loss')
    plt.legend()
    plt.show()


positive_tweets = twitter_samples.strings("positive_tweets.json")
negative_tweets = twitter_samples.strings("negative_tweets.json")

# Reset the tweet preprocessor to it's default settings
tweet_preprocessor.set_options(tweet_preprocessor.OPT.URL,
                               tweet_preprocessor.OPT.MENTION,
                               tweet_preprocessor.OPT.HASHTAG,
                               tweet_preprocessor.OPT.RESERVED,
                               tweet_preprocessor.OPT.NUMBER,
                               tweet_preprocessor.OPT.EMOJI,
                               tweet_preprocessor.OPT.SMILEY,
                               )

cleaned_postive_tweets = [tweet_preprocessor.clean(html.unescape(x)) for x in positive_tweets]
cleaned_negative_tweets = [tweet_preprocessor.clean(html.unescape(x)) for x in negative_tweets]

training_tweets = positive_tweets[0:4000] + negative_tweets[0:4000]
test_tweets = positive_tweets[4000:] + negative_tweets[4000:]

tokenizer = Tokenizer(num_words=5000, filters="\t\n")
tokenizer.fit_on_texts(training_tweets)

X_train = tokenizer.texts_to_sequences(training_tweets)
X_test = tokenizer.texts_to_sequences(test_tweets)

y_train = [1] * 4000 + [0] * 4000
y_test = [1] * 1000 + [0] * 1000

vocab_size = len(tokenizer.word_index) + 1
maxlen = 100

X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)
X_test = pad_sequences(X_test, padding='post', maxlen=maxlen)

embedding_dim = 100

model = Sequential()
model.add(layers.Embedding(vocab_size, embedding_dim, input_length=maxlen))
model.add(layers.Conv1D(128, 5, activation='relu'))
model.add(layers.GlobalMaxPooling1D())
model.add(layers.Dense(10, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train,
                    epochs=10,
                    verbose=False,
                    batch_size=10,
                    validation_split=0.1)


class SentimentIntensityAnalyzerWrapper(ClassifierI):
    def __init__(self, keras_model):
        self.sid = SentimentIntensityAnalyzer()
        self.keras_model = keras_model

    def classify_many(self, featuresets):
        results = []
        for features in featuresets:
            sentiment_scores = self.keras_model.predict_classes(numpy.array([features]))
            results.append(sentiment_scores[0][0])
        return results


siaw = SentimentIntensityAnalyzerWrapper(model)
sentim_analyzer = SentimentAnalyzer()

for key, value in sorted(sentim_analyzer.evaluate([(x, y) for (x, y) in zip(X_test, y_test)], classifier=siaw).items()):
    print('{0}: {1}'.format(key, value))

plot_history(history)