f = open("c:\\data\\book.text", "r")
s = f.read()
print(s)

# Dictionary conversion from text(json) to python dictionary
import json
book = json.loads(s)

print(book)

print(type(book))

print(book["bob"])
print(book["bob"]["phone"])

for person in book:
    print(book[person])