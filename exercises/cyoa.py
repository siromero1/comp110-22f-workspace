"""Create Your Own Adventure Experience."""

__author__ = "730576249"


from random import randint


points: int = 10
player: str = ""


def main() -> None:
    """The entrypoint of the program."""
    greet()
    user_continue: str = input("Would you like to continue (Y/N)? ")
    if user_continue != "Y":
        print("Game ended.\nTotal points: 0")
    level_input: str = input("There are 3 levels to choose from:\neasy, medium, and hard\nOr to end game: enter end game. Which would you like to choose? ")
    if level_input == "easy":
        users_guess_10()
    if level_input == "medium":
        users_guess_25()
    if level_input == "hard":
        users_guess_50()
    if level_input == "end game":
        print("Game over. Have a good day!")
    return None


def greet() -> None:
    """Greeting the player."""
    HEART_EMOJI: str = "\U00002764"
    global player
    player = input("What is your name? ")
    print(f"Welcome {player}{HEART_EMOJI}\nThe goal is to guess the secret number is least amount of guesses possible.\nThe secret number is a randomly generated number 0 to 10.\nA point is deducted after each guess.")


def users_guess_10(secret_number: int = randint(0, 10)) -> int:
    """Easy difficulty game option."""
    compare_guess: int = int(input("What is your guess (0-10)? "))
    PARTY_EMOJI: str = "\U0001F973"
    global points
    points = 10
    while points > 0:
        if compare_guess == secret_number:
            print(f"Winner{PARTY_EMOJI}! You correctly guessed the secret number!\nTotal points: {points}")
            return points
        else:
            compare_guess = int(input(f"Sorry {player}, that is incorrect. Guess again: "))
            if compare_guess > secret_number:
                print(f"Guess lower, {player}.")
            if compare_guess < secret_number:
                print(f"Guess higher, {player}.")
        points = points - 1
    print(f"Sorry, {player}. You ran out of points! Game over.\nThanks for playing!")
    return points


def users_guess_25(hidden_number: int = randint(0, 25)) -> None:
    """Medium difficulty game option."""
    comp_guess: int = int(input("What is your guess (0-25)? "))
    PARTY_EMOJI: str = "\U0001F973"
    global points
    points = 25
    while points > 0:
        if comp_guess == hidden_number:
            return print(f"Winner{PARTY_EMOJI}! You correctly guessed the secret number\nTotal points: {points}")
        else:
            comp_guess = int(input(f"Sorry {player}, that is incorrect. Guess again: "))
            if comp_guess > hidden_number:
                print(f"Guess lower, {player}.")
            if comp_guess < hidden_number:
                print(f"Guess higher, {player}.")
        points = points - 2
    return print(f"Sorry, {player}. You ran out of points! Game over.\nThanks for playing!")


def users_guess_50(a_secret_number: int = randint(0, 50)) -> None:
    """Hard difficulty game option."""
    comparing_guess: int = int(input("What is your guess (0-50)? "))
    PARTY_EMOJI: str = "\U0001F973"
    global points
    points = 50
    while points > 50:
        if comparing_guess == a_secret_number:
            return print(f"Winner{PARTY_EMOJI}! You correctly guessed the secret number\nTotal points: {points}")
        else:
            comparing_guess = int(input(f"Sorry {player}, that is incorrect. Guess again: "))
            if comparing_guess > a_secret_number:
                print(f"Guess lower, {player}.")
            if comparing_guess < a_secret_number:
                print(f"Guess higher, {player}.")
        points = points - 5
    return print(f"Sorry, {player}. You ran out of points! Game over.\nThanks for playing!")


if __name__ == "__main__":
    main()