from mongoengine import connect, Document, StringField, ListField, URLField

# Establishing a Connection
connect(db="rpblog", host="localhost", port=27017)


# Defining a Document Schema or Model
class Posts(Document):
    title = StringField(required=True, max_length=70)
    author = StringField(required=True, max_length=20)
    contributors = ListField(StringField(max_length=20))
    url = URLField(required=True)


# Creating and Saving Documents
post = Posts(
    title="Beautiful Soup: Build a Web Scraper With Python",
    author="Martin",
    contributors=["Aldren", "Geir", "Jaya", "Joanna", "Mike"],
    url="https://realpython.com/beautiful-soup-web-scraper-python/"
)
post.save()  # Insert the new post

# Retrieving All the Documents
for post in Posts.objects:
    print(post.title)

# Filtering Documents by Author
for post in Posts.objects(author="Alex"):
    print(post.title)
