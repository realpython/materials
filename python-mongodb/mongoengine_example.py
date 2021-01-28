from mongoengine import Document, ListField, StringField, URLField, connect

# Establishing a Connection
connect(db="rpblog", host="localhost", port=27017)


# Defining a Document Schema or Model
class Post(Document):
    title = StringField(required=True, max_length=70)
    author = StringField(required=True, max_length=20)
    contributors = ListField(StringField(max_length=20))
    url = URLField(required=True)


# Creating and Saving Documents
post1 = Post(
    title="Beautiful Soup: Build a Web Scraper With Python",
    author="Martin",
    contributors=["Aldren", "Geir", "Jaya", "Joanna", "Mike"],
    url="https://realpython.com/beautiful-soup-web-scraper-python/",
)
post1.save()  # Insert the new post

# Retrieving All the Documents' title
for doc in Post.objects:
    print(doc.title)

# Filtering Documents by Author
for doc in Post.objects(author="Alex"):
    print(doc.title)
