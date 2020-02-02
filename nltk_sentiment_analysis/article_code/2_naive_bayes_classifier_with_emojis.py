import html

import nltk
import preprocessor as tweet_preprocessor
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import twitter_samples
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import extract_unigram_feats

tweet_preprocessor.set_options(tweet_preprocessor.OPT.URL,
                               tweet_preprocessor.OPT.MENTION,
                               tweet_preprocessor.OPT.HASHTAG,
                               tweet_preprocessor.OPT.RESERVED,
                               tweet_preprocessor.OPT.NUMBER)

positive_tweets = twitter_samples.strings("positive_tweets.json")
negative_tweets = twitter_samples.strings("negative_tweets.json")

cleaned_postive_tweets = [tweet_preprocessor.clean(html.unescape(x)) for x in positive_tweets]
cleaned_negative_tweets = [tweet_preprocessor.clean(html.unescape(x)) for x in negative_tweets]

labeled_positive_tweets = [(nltk.word_tokenize(x), 1) for x in cleaned_postive_tweets]
labeled_negative_tweets = [(nltk.word_tokenize(x), 0) for x in cleaned_negative_tweets]

training_samples = labeled_positive_tweets[0:4000] + labeled_negative_tweets[0:4000]
test_samples = labeled_positive_tweets[4000:] + labeled_negative_tweets[4000:]

sentim_analyzer = SentimentAnalyzer()
all_words = []
for tweet, sentiment_score in training_samples:
    for word in tweet:
        all_words.append(word)

feature_words = sentim_analyzer.unigram_word_feats(all_words, min_freq=10)
sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=feature_words)

training_set = sentim_analyzer.apply_features(training_samples)
test_set = sentim_analyzer.apply_features(test_samples)

trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)
for key, value in sorted(sentim_analyzer.evaluate(test_set).items()):
    print('{0}: {1}'.format(key, value))
