PATH = "books/frankenstein.txt"

with open(PATH) as f:
    contents = f.read()
    word_count = len(contents.split(" "))
print(word_count)
