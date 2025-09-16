from art import logo
import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    difficulty = input("choose a difficulty, type 'easy' or 'hard' ").lower()
    if difficulty == "easy":
        return EASY_LEVEL_TURNS
    elif difficulty == "hard":
        return HARD_LEVEL_TURNS


def check_answer(answer, number, attempts):
    if number > answer:
        print("to low!")
        print("Guess again")
        return attempts - 1
    elif number < answer:
        print("to high!")
        print("Guess again")
        return attempts - 1
    else:
        print(f"you got it the answer was {number}")
        return 0


print(logo)
print("Welcome to the Number guessing game!")
print("iam thinking of number between 1 and 100")
game_end = False
GuessNumber = random.randint(1, 100)
attempts = set_difficulty()
while not game_end:
    print(f"you have {attempts} attempts left")
    Playerguess = int(input("Make a guess : "))
    attempts = check_answer(Playerguess, GuessNumber, attempts)
    if attempts == 0:
        game_end = True
