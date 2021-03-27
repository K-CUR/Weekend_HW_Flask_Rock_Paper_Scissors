import unittest
from models.game import Game
from models.player import Player

class TestGame (unittest.TestCase):


# I had to bring the function in here as if I tried to test it from game.py and in the test wrote 
# actual = self.who_wins(player_1, player_2), I got an error saying 'TestGame' object has no attribute 'models'

# FUNCTION TO TEST
    def who_wins(self, player1_choice, player2_choice):
        choice_1 = player1_choice
        choice_2 = player2_choice

        if choice_1 == "rock" and choice_2 == "rock" or choice_1 == "paper" and choice_2 == "paper" or choice_1 == "scissors" and choice_2 == "scissors":
            return "It's a draw"

        elif choice_1 == "rock" and choice_2 == "scissors" or choice_1 == "paper" and choice_2 == "rock" or choice_1 == "scissors" and choice_2 == "paper":
            return "Player 1 wins! " + choice_1 + " beats " + choice_2

        elif choice_1 == "rock" and choice_2 == "paper" or choice_1 == "paper" and choice_2 == "scissors" or choice_1 == "scissors" and choice_2 == "rock":
            return "Player 2 wins! " + choice_2 + " beats " + choice_1

# TEST 1
    def test_game_gives_result_1(self):
        player1_choice = "paper"
        player2_choice = "paper"
        actual = self.who_wins(player1_choice, player2_choice)
        expected = "It's a draw"
        self.assertEqual(expected, actual)

# TEST 2
    def test_game_gives_result_2(self):
        player1_choice = "rock"
        player2_choice = "scissors"
        actual = self.who_wins(player1_choice, player2_choice)
        expected = "Player 1 wins! rock beats scissors"
        self.assertEqual(expected, actual)

# TEST 3
    def test_game_gives_result_3(self):
        player1_choice = "paper"
        player2_choice = "scissors"
        actual = self.who_wins(player1_choice, player2_choice)
        expected = "Player 2 wins! scissors beats paper"
        self.assertEqual(expected, actual)