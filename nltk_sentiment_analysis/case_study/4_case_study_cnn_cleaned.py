import html

import numpy
import pandas as pd
import preprocessor as tweet_preprocessor
from keras import Sequential, layers
from keras.preprocessing.sequence import pad_sequences
from keras_preprocessing.text import Tokenizer
from nltk.corpus import twitter_samples

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

tokenizer = Tokenizer(num_words=5000, filters="\t\n")
tokenizer.fit_on_texts(training_tweets)

X_train = tokenizer.texts_to_sequences(training_tweets)
y_train = [1] * 4000 + [0] * 4000

vocab_size = len(tokenizer.word_index) + 1
maxlen = 100

X_train = pad_sequences(X_train, padding='post', maxlen=maxlen)

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

results_dict = dict(
    {
        "Airline": list(),
        "Positive Sentiment Count": list(),
        "Negative Sentiment Count": list()
    }
)

airline_friendly_name_map = {
    "americanair": "American Airlines",
    "united": "United Airlines",
    "southwestair": "Southwest Airlines",
    "delta": "Delta"
}

for airline_name in ["americanair", "united", "southwestair", "delta"]:
    with open("case_study_dataset_{}.csv".format(airline_name), "r") as file_handle:
        next(file_handle)  # Skip the header
        dataset = list()
        for line in file_handle.readlines():
            dataset.append(tweet_preprocessor.clean(html.unescape(line)))

    positive_sentiment_count = 0
    negative_sentiment_count = 0

    dataset = tokenizer.texts_to_sequences(dataset)
    dataset = pad_sequences(dataset, padding='post', maxlen=maxlen)

    for tweet in dataset:
        sentiment_score = model.predict_classes(numpy.array([tweet]))
        if sentiment_score[0][0] == 0:
            negative_sentiment_count = negative_sentiment_count + 1
        else:
            positive_sentiment_count = positive_sentiment_count + 1

    results_dict["Airline"].append(airline_friendly_name_map[airline_name])
    results_dict["Positive Sentiment Count"].append(positive_sentiment_count)
    results_dict["Negative Sentiment Count"].append(negative_sentiment_count)

pd.DataFrame(results_dict).to_csv("case_study_cnn_cleaned.csv")
