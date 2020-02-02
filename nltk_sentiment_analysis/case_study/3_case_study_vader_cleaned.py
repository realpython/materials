import html

import pandas as pd
import preprocessor as tweet_preprocessor
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Reset the tweet preprocessor to it's default settings
tweet_preprocessor.set_options(tweet_preprocessor.OPT.URL,
                               tweet_preprocessor.OPT.MENTION,
                               tweet_preprocessor.OPT.HASHTAG,
                               tweet_preprocessor.OPT.RESERVED,
                               tweet_preprocessor.OPT.NUMBER,
                               tweet_preprocessor.OPT.EMOJI,
                               tweet_preprocessor.OPT.SMILEY,
                               )

sia = SentimentIntensityAnalyzer()

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
    neutral_sentiment_count = 0
    for tweet in dataset:
        sentiment_scores = sia.polarity_scores(tweet)
        if sentiment_scores["compound"] <= -0.05:
            negative_sentiment_count = negative_sentiment_count + 1
        else:
            positive_sentiment_count = positive_sentiment_count + 1

    results_dict["Airline"].append(airline_friendly_name_map[airline_name])
    results_dict["Positive Sentiment Count"].append(positive_sentiment_count)
    results_dict["Negative Sentiment Count"].append(negative_sentiment_count)

pd.DataFrame(results_dict).to_csv("case_study_vader_cleaned.csv")
