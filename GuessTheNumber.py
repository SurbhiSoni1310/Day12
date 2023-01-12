from art import logo
import random
from time import sleep

chosen = random.randint(1, 100)


# print("Secret : " + str(chosen))


def play_game(chances):
    while chances != 0:
        num = int(input("Guess the number : "))
        if chances == 1 and chosen != num:
            print("You Lose :(")
            chances -= 1
            print(f"The number was {chosen}")
            sleep(10)
        elif num == chosen:
            print("You have won this game! Congrats :) ")
            sleep(10)
            return
        elif abs(chosen - num) <= 5:
            print("You are very close but unfortunately not there!!")
            chances -= 1
            print(f"You have {chances} chances left")
        elif num > chosen:
            print("Too high\nTry Again")
            chances -= 1
            print(f"You have {chances} chances left")
        elif num < chosen:
            print("Too Less\nTry again")
            chances -= 1
            print(f"You have {chances} chances left")
        else:
            continue


print(logo)
print("Welcome to the Guess the number game!")
print("Computer has chosen any number between 1-100 (both included)")
print("You have to guess the number")

EASY = 10
HARD = 5
level = input("Enter the level you want to play (easy/hard) : ").lower()
if level == "easy":
    print("You have 10 chances to guess the number")
    play_game(EASY)
elif level == "hard":
    print("You have 5 chances to guess the word")
    play_game(HARD)
else:
    print("Wrong input. Program Terminated")
    sleep(10)
