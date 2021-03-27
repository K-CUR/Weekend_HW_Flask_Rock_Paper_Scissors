from models.game import *


def who_wins(player1_choice, player2_choice):
    choice_1 = player1_choice
    choice_2 = player2_choice

    if choice_1 == "rock" and choice_2 == "rock" or choice_1 == "paper" and choice_2 == "paper" or choice_1 == "scissors" and choice_2 == "scissors":
        return "It's a draw"

    elif choice_1 == "rock" and choice_2 == "scissors" or choice_1 == "paper" and choice_2 == "rock" or choice_1 == "scissors" and choice_2 == "paper":
        return "Player 1 wins! " + str.capitalize(choice_1) + " beats " + choice_2

    elif choice_1 == "rock" and choice_2 == "paper" or choice_1 == "paper" and choice_2 == "scissors" or choice_1 == "scissors" and choice_2 == "rock":
        return "Player 2 wins! " + str.capitalize(choice_2) + " beats " + choice_1