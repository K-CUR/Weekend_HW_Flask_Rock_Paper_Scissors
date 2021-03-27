import unittest
from models.game import Game
from models.player import Player

class TestGame (unittest.TestCase):


# I had to bring the function in here as if I tried to test it from game.py and in the test wrote 
# actual = self.who_wins(player_1, player_2), I got an error saying 'TestGame' object has no attribute 'models'

# FUNCTION TO TEST
    def who_wins(self, player_1, player_2):
        choice_1 = player_1.choice
        choice_2 = player_2.choice

        if choice_1 == "rock" and choice_2 == "rock" or choice_1 == "paper" and choice_2 == "paper" or choice_1 == "scissors" and choice_2 == "scissors":
            return "It's a draw"

        elif choice_1 == "rock" and choice_2 == "scissors" or choice_1 == "paper" and choice_2 == "rock" or choice_1 == "scissors" and choice_2 == "paper":
            return player_1.name + " wins! " + player_1.choice + " beats " + player_2.choice

        elif choice_1 == "rock" and choice_2 == "paper" or choice_1 == "paper" and choice_2 == "scissors" or choice_1 == "scissors" and choice_2 == "rock":
            return player_2.name + " wins! " + player_2.choice + " beats " + player_1.choice

# TEST 1
    def test_game_gives_result_1(self):
        player_1 = Player("Annie", "paper")
        player_2 = Player("Bertie", "paper")
        actual = self.who_wins(player_1, player_2)
        expected = "It's a draw"
        self.assertEqual(expected, actual)

# TEST 2
    def test_game_gives_result_2(self):
        player_1 = Player("Annie", "rock")
        player_2 = Player("Bertie", "scissors")
        actual = self.who_wins(player_1, player_2)
        expected = "Annie wins! rock beats scissors"
        self.assertEqual(expected, actual)

# TEST 3
    def test_game_gives_result_3(self):
        player_1 = Player("Annie", "paper")
        player_2 = Player("Bertie", "scissors")
        actual = self.who_wins(player_1, player_2)
        expected = "Bertie wins! scissors beats paper"
        self.assertEqual(expected, actual)