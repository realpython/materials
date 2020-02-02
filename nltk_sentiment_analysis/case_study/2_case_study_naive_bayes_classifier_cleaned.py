import html

import nltk
import pandas as pd
import preprocessor as tweet_preprocessor
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import twitter_samples
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import extract_unigram_feats

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

labeled_positive_tweets = [(nltk.word_tokenize(x), 1) for x in cleaned_postive_tweets]
labeled_negative_tweets = [(nltk.word_tokenize(x), 0) for x in cleaned_negative_tweets]

training_samples = labeled_positive_tweets[0:4000] + labeled_negative_tweets[0:4000]

sentim_analyzer = SentimentAnalyzer()
all_words = []
for tweet, sentiment_score in training_samples:
    for word in tweet:
        all_words.append(word)

feature_words = sentim_analyzer.unigram_word_feats(all_words, min_freq=10)
sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=feature_words)

training_set = sentim_analyzer.apply_features(training_samples)

trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)

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
            dataset.append(nltk.word_tokenize(tweet_preprocessor.clean(html.unescape(line))))

    positive_sentiment_count = 0
    negative_sentiment_count = 0

    for tweet in dataset:
        sentiment_score = sentim_analyzer.classify(tweet)
        if sentiment_score == 0:
            negative_sentiment_count = negative_sentiment_count + 1
        else:
            positive_sentiment_count = positive_sentiment_count + 1

    results_dict["Airline"].append(airline_friendly_name_map[airline_name])
    results_dict["Positive Sentiment Count"].append(positive_sentiment_count)
    results_dict["Negative Sentiment Count"].append(negative_sentiment_count)

pd.DataFrame(results_dict).to_csv("case_study_naive_bayes_classifier_cleaned.csv")
