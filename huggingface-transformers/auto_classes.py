import torch
from transformers import (
    AutoConfig,
    AutoModelForSequenceClassification,
    AutoTokenizer,
)

model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"

config = AutoConfig.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "I love using the Transformers library!"
encoded_input = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    output = model(**encoded_input)

scores = output.logits[0]
probabilities = torch.softmax(scores, dim=0)

for i, prob in enumerate(probabilities):
    label = config.id2label[i]
    print(f"{i + 1}) {label}: {prob}")
