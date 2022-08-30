"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730576249"

user_name: str = input("Enter a 5-character word: ")
letter: str = input("Enter a single character: ")

print("Searching for " + letter + " in " + user_name)

if letter == user_name [0]:
    print(letter + " found at index 0")
if letter == user_name [1]:
    print(letter + " found at index 1")
if letter == user_name [2]:
    print(letter + " found at index 2")
if letter == user_name [3]:
    print(letter + " found at index 3")
if letter == user_name [4]:
    print(letter + " found at index 4")

