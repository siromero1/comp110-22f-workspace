"""EX03 - Structured - Wordle."""

__author__ = "730576249"

def contains_char(word: str, character: str) -> bool:  # defining contains_char to find a matching character in the word
    """Finding a matching character in the word."""
    assert len(character) == 1
    i: int = 0
    while i < len(word): 
        if character == word[i]:
            return True
        i = i + 1
    return False

def emojified(guess: str, secret: str) -> str:  # defining emojified to correspond colored emoji boxes with matching characters
    """Corresponding colored emoji boxes."""
    i: int = 0
    emoji: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    assert len(guess) == len(secret)
    while i < len(guess):
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        else:
            if contains_char(secret, guess[i]) is True:
                emoji += YELLOW_BOX
            if contains_char(secret, guess[i]) is False:
                emoji += WHITE_BOX
        i = i + 1
    return emoji

def input_guess(exp_len: int) -> str:  # comparing the length of secret word to input
    """Comparing input and secret word length."""
    guess_len: str = input(f"Enter a {exp_len} character word: ")
    while len(guess_len) != exp_len:
        guess_len: str = input(f"That wasn't {exp_len} chars! Try again: ")
    return guess_len

def main() -> None:  # pulling together the functions
    """The entrypoint of the program and main game loop."""
    user_input:str = ""
    secret_word:str = "codes"
    i: int = 0
    turn_number: int  = 1
    while turn_number <= 6 and user_input != secret_word:
        print(f" === Turn {turn_number}/6 === ")
        user_input: str = input("Enter a 5 character word: ")
        emoji: str = emojified(user_input, secret_word)
        print(emoji)
        if user_input != secret_word:
            turn_number += 1
    if user_input == secret_word:
        print(f"You won in {turn_number}/6 turns!")
    if user_input != secret_word:
        print("X/6 - Sorry try again tomorrow!")



if __name__ == "__main__":  # making it possible to run Python program as a module
    main()