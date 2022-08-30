"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730576249"

user_name: str = input("Enter a 5-character word: ")
letter: str = input("Enter a single character: ")

print("Searching for " + letter + " in " + user_name)
print(letter + " found at index")