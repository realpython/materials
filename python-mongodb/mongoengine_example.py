from mongoengine import Document, ListField, StringField, URLField, connect

# Establish a connection
connect(db="rptutorials", host="localhost", port=27017)


# Define a document schema or model
class Tutorial(Document):
    title = StringField(required=True, max_length=70)
    author = StringField(required=True, max_length=20)
    contributors = ListField(StringField(max_length=20))
    url = URLField(required=True)


# Create and save documents
tutorial1 = Tutorial(
    title="Beautiful Soup: Build a Web Scraper With Python",
    author="Martin",
    contributors=["Aldren", "Geir", "Jaya", "Joanna", "Mike"],
    url="https://realpython.com/beautiful-soup-web-scraper-python/",
)
tutorial1.save()  # Insert the new tutorial

# Retrieving all documents and print their title
for doc in Tutorial.objects:
    print(doc.title)

# Filtering documents by author
for doc in Tutorial.objects(author="Alex"):
    print(doc.title)
