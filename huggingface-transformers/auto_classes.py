import torch
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    pipeline,
)

model_name = "cardiffnlp/twitter-roberta-base-sentiment-latest"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "I love using the Transformers library!"
encoded_input = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    output = model(**encoded_input)

scores = output.logits[0]
probabilities = torch.softmax(scores, dim=0)
predicted_class = probabilities.argmax().item()

print(f"Predicted class: {predicted_class}")
print(f"Probabilities: {probabilities.tolist()}")

full_pipeline = pipeline(model=model_name)
print(full_pipeline(text))
