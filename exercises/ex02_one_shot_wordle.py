"""EX02 - One-Shot - Wordle."""

__author__ = "730576249"

secret_word: str = "python" # declaring the secret word "python"

i: int = 0 # declaring varibales for while loops
emoji: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

guess: str = input("What is your 6-letter guess? ") # asking for user input

while len(guess) != len("python"):
    guess = input("That was not 6 letters! Try again: ")


while i < len(guess): # matching letters in the same index will result in a green box
    if guess[i] == secret_word[i]:
        emoji += GREEN_BOX
    else: 
        guess_exists: bool = False
        alt_indicies: int = 0
        while guess_exists == False and alt_indicies < len(secret_word):
            if guess[i] == secret_word[alt_indicies]:
                guess_exists = True
            alt_indicies += 1
        if guess_exists == True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX
    i += 1 #continue to increase index to move on to next letter in guess


print(emoji) # printing result of matching indices as emojis
if guess != secret_word:
    print("Not quite. Play again soon! ")
if guess == secret_word:
    print("Woo! You got it!")