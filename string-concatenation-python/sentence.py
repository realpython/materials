from io import StringIO

sentence = StringIO()
while True:
    word = input("Enter a word (or './!/?' to end the sentence): ")
    if word in ".!?":
        sentence.write(word)
        break
    if sentence.tell() == 0:
        sentence.write(word)
    else:
        sentence.write(" " + word)

print("The concatenated sentence is:", sentence.getvalue())
