from transformers import pipeline

model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"
sentiment_classifier = pipeline(model=model_name)

text_input = "I'm really excited about using HuggingFace to run AI models!"
print(sentiment_classifier(text_input))

text_input = "I'm having a horrible day today."
print(sentiment_classifier(text_input))

text_input = "Most of the Earth is covered in water."
print(sentiment_classifier(text_input))

text_inputs = [
    "What a great time to be alive!",
    "How are you doing today?",
    "I'm in a horrible mood.",
]

print(sentiment_classifier(text_inputs))

model_name = "MoritzLaurer/deberta-v3-large-zeroshot-v2.0"
zs_text_classifier = pipeline(model=model_name)

candidate_labels = [
    "Billing Issues",
    "Technical Support",
    "Account Information",
    "General Inquiry",
]

hypothesis_template = "This text is about {}"

customer_text = "My account was charged twice for a single order."
print(
    zs_text_classifier(
        customer_text,
        candidate_labels,
        hypothesis_template=hypothesis_template,
        multi_label=True,
    )
)

image_classifier = pipeline(task="image-classification")

preds = image_classifier(["llamas.png"])
print(len(preds[0]))

print(preds[0][0])

print(preds[0][1])

print(preds[0][2])
