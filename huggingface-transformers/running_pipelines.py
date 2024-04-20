from transformers import pipeline

# Sentiment analysis example
task = "text-classification"
sentiment_model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
sentiment_classifier = pipeline(task=task, model=sentiment_model_name)

text_input = "I really loved this product!"
sentiment_classifier(text_input)

text_input = "Joe went to the park."
sentiment_classifier(text_input)

text_input = "This product was terrible and it didn't work at all!"
sentiment_classifier(text_input)

# Zero-shot classification example
task = "zero-shot-classification"
zs_model_name = "facebook/bart-large-mnli"
zs_text_classifier = pipeline(task=task, model=zs_model_name)

candidate_labels = [
    "Quality",
    "Value for Money",
    "Durability",
    "Ease of Use",
    "Customer Service",
    "Delivery",
    "Packaging",
    "Product Features",
    "Comparison",
    "Repeat Purchase",
    "Recommendation",
    "Safety",
    "Environmental Impact",
]

review = (
    "Highly recommend! This product was easy to use and well worth the price."
)

zs_text_classifier(review, candidate_labels, multilabel=True)
