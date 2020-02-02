from nltk.corpus import twitter_samples
positive_tweets = twitter_samples.strings("positive_tweets.json")
negative_tweets = twitter_samples.strings("negative_tweets.json")
print(type(positive_tweets))
print(type(negative_tweets))

print("\n~x~\n")

print(len(positive_tweets), len(negative_tweets))

print()

for num, tweet in enumerate(positive_tweets[0:5]):
    print("#{} => {}".format(num, tweet))

print()

for num, tweet in enumerate(negative_tweets[0:5]):
    print("#{} => {}".format(num, tweet))

print("\n~x~\n")

import preprocessor as tweet_preprocessor
import html

cleaned_postive_tweets = [tweet_preprocessor.clean(html.unescape(x)) for x in positive_tweets]
cleaned_negative_tweets = [tweet_preprocessor.clean(html.unescape(x)) for x in negative_tweets]

for num, tweet in enumerate(cleaned_postive_tweets[0:5]):
    print("#{} => {}".format(num, tweet))

print()

for num, tweet in enumerate(cleaned_negative_tweets[0:5]):
    print("#{} => {}".format(num, tweet))

print("\n~x~\n")

import nltk

labeled_positive_tweets = [(nltk.word_tokenize(x), 1) for x in cleaned_postive_tweets]
labeled_negative_tweets = [(nltk.word_tokenize(x), 0) for x in cleaned_negative_tweets]

print("Sample positive tweet: {}".format(labeled_positive_tweets[0]))
print("Sample negative tweet: {}".format(labeled_negative_tweets[0]))

print("\n~x~\n")

training_samples = labeled_positive_tweets[0:4000] + labeled_negative_tweets[0:4000]
test_samples = labeled_positive_tweets[4000:] + labeled_negative_tweets[4000:]

print("\n~x~\n")

from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import extract_unigram_feats

sentim_analyzer = SentimentAnalyzer()
all_words = []
for tweet, sentiment_score in training_samples:
    for word in tweet:
        all_words.append(word)

feature_words = sentim_analyzer.unigram_word_feats(all_words, min_freq=10)
sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=feature_words)
print(len(feature_words))

print("\n~x~\n")

training_set = sentim_analyzer.apply_features(training_samples)
print(type(training_set))
print(len(training_set))
test_set = sentim_analyzer.apply_features(test_samples)
print(type(test_set))
print(len(test_set))

print("Investigating the training set: ")
print(type(training_set[0]), len(training_set[0]), training_set[0])
print("Investigating the test set: ")
print(type(test_set[0]), len(test_set[0]), test_set[0])

print("\n~x~\n")

from nltk.classify import NaiveBayesClassifier

trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)
for key, value in sorted(sentim_analyzer.evaluate(test_set).items()):
    print('{0}: {1}'.format(key, value))

print("\n~x~\n")