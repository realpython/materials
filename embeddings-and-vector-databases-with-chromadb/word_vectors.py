import spacy

from cosine_similarity import compute_cosine_similarity

# Load the medium-size English model
nlp = spacy.load("en_core_web_md")

# Get the word vector for the word "dog"
dog_embedding = nlp.vocab["dog"].vector

# Word vectors are stored as NumPy arrays
print(type(dog_embedding))

# Word vector dimension
print(dog_embedding.shape)

# First 10 elements of the "dog" word vector
print(dog_embedding[0:10])

dog_embedding = nlp.vocab["dog"].vector
cat_embedding = nlp.vocab["cat"].vector
apple_embedding = nlp.vocab["apple"].vector
tasty_embedding = nlp.vocab["tasty"].vector
delicious_embedding = nlp.vocab["delicious"].vector
truck_embedding = nlp.vocab["truck"].vector

print(compute_cosine_similarity(dog_embedding, cat_embedding))

print(compute_cosine_similarity(delicious_embedding, tasty_embedding))

print(compute_cosine_similarity(apple_embedding, delicious_embedding))

print(compute_cosine_similarity(dog_embedding, apple_embedding))

print(compute_cosine_similarity(truck_embedding, delicious_embedding))
