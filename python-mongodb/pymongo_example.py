import pprint

from pymongo import MongoClient

# Establishing a Connection
client = MongoClient("localhost", 27017)

# Accessing Databases
db = client.rpblog

# Accessing Collections
posts = db.posts

# Inserting a Single Document
post = {
    "title": "Working With JSON Data in Python",
    "author": "Lucas",
    "contributors": ["Aldren", "Dan", "Joanna"],
    "url": "https://realpython.com/python-json/",
}
result = posts.insert_one(post)
print(f"One post: {result.inserted_id}")

# Inserting Several Documents
post_1 = {
    "title": "Python’s Requests Library (Guide)",
    "author": "Alex",
    "contributors": [
        "Aldren",
        "Brad",
        "Joanna"
    ],
    "url": "https://realpython.com/python-requests/"
}

post_2 = {
    "title": "Object-Oriented Programming (OOP) in Python 3",
    "author": "David",
    "contributors": [
        "Aldren",
        "Joanna",
        "Jacob"
    ],
    "url": "https://realpython.com/python3-object-oriented-programming/"
}

new_result = posts.insert_many([post_1, post_2])
print(f"Multiple posts: {new_result.inserted_ids}")

# Retrieving All Documents
for doc in posts.find():
    pprint.pprint(doc)

# Retrieving a Single Document
jon_post = posts.find_one({"author": "Jon"})
pprint.pprint(jon_post)

# Closing a Connection
with MongoClient() as client:
    db = client.rpblog
    for doc in db.posts.find():
        pprint.pprint(doc)
