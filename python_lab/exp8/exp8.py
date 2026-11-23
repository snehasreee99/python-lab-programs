import re

text = input("Enter a sentence: ")

word = input("Enter word to search: ")

# Search for a word
result = re.search(word, text)

if result:
    print("Word Found")
else:
    print("Word Not Found")

# Find all digits
digits = re.findall("[0-9]", text)
print("Digits:", digits)

# Find all words
words = re.findall("[A-Za-z]+", text)
print("Words:", words)

# Check starting word
result = re.match(word, text)

if result:
    print("Sentence starts with the given word")
else:
    print("Sentence does not start with the given word")
