import pprint

from pymongo import MongoClient

# Establishing a Connection
client = MongoClient("localhost", 27017)

# Accessing Databases
db = client.rpblog

# Accessing Collections
post = db.post

# Inserting a Single Document
post1 = {
    "title": "Working With JSON Data in Python",
    "author": "Lucas",
    "contributors": ["Aldren", "Dan", "Joanna"],
    "url": "https://realpython.com/python-json/",
}
result = post.insert_one(post1)
print(f"One post: {result.inserted_id}")

# Inserting Several Documents
post2 = {
    "title": "Python’s Requests Library (Guide)",
    "author": "Alex",
    "contributors": ["Aldren", "Brad", "Joanna"],
    "url": "https://realpython.com/python-requests/",
}

post3 = {
    "title": "Object-Oriented Programming (OOP) in Python 3",
    "author": "David",
    "contributors": ["Aldren", "Joanna", "Jacob"],
    "url": "https://realpython.com/python3-object-oriented-programming/",
}

new_result = post.insert_many([post2, post3])
print(f"Multiple posts: {new_result.inserted_ids}")

# Retrieving All Documents
for doc in post.find():
    pprint.pprint(doc)

# Retrieving a Single Document
jon_post = post.find_one({"author": "Jon"})
pprint.pprint(jon_post)

# Closing a Connection
with MongoClient() as client:
    db = client.rpblog
    for doc in db.post.find():
        pprint.pprint(doc)
