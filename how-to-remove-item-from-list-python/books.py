books = ["Dragonsbane", "The Hobbit", "Wonder", "Jaws"]
print(books.pop(0))
print(books)

books = ["Dragonsbane", "The Hobbit", "Wonder", "Jaws"]
read_books = []
read = books.pop(0)
read_books.append(read)
print(read_books)
print(books)

books = ["Dragonsbane", "The Hobbit", "Wonder", "Wonder", "Jaws", "Jaws"]
del books[2]
print(books)
del books[-1]
print(books)

books = ["Dragonsbane", "The Hobbit", "Wonder", "Jaws"]
books.remove("The Hobbit")
print(books)

# books = ["Dragonsbane", "The Hobbit", "Wonder", "Jaws"]
# books.remove("The Two Towers")
# print(books)

books = ["Dragonsbane", "The Hobbit", "Wonder", "Jaws"]
del books[0:3]
print(books)

books = ["Dragonsbane", "The Hobbit", "Wonder", "Jaws", "It"]
del books[-3:-1]
print(books)

books = ["Dragonsbane", "The Hobbit", "Wonder", "Jaws", "It"]
books.clear()
print(books)
