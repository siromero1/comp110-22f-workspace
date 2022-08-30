"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730576249"

word: str = input("Enter a 5-character word: ")
letter: str = input("Enter a single character: ")

print("Searching for " + letter + " in " + word)

if letter == word[0]:
    print(letter + " found at index 0")
if letter == word[1]:
    print(letter + " found at index 1")
if letter == word[2]:
    print(letter + " found at index 2")
if letter == word[3]:
    print(letter + " found at index 3")
if letter == word[4]:
    print(letter + " found at index 4")

count: int = len("word")

if letter == count(0):
    print("No instances of " + letter + "found in " + word)
if letter == count(1):
    print("1 instance of " + letter + "found in " + word)
if letter == count(2):
    print("2 instances of " + letter + "found in " + word)
if letter == count(3):
    print("3 instances of " + letter + "found in " + word)
if letter == count(4):
    print("4 instances of " + letter + "found in " + word)
if letter == count(5):
    print("5 instances of " + letter + "found in " + word)

char: str
if char < 5:
    print("Error: Word must contain 5 characters")
if char > 5:
    print("Error: Word must conatin 5 characters")