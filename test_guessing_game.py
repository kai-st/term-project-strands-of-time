import io
from unittest import TestCase
from unittest.mock import patch


import game


class TestGuessingGame(TestCase):

    @patch('game.pick_type_of_foe', return_value="drow")
    @patch('builtins.input', side_effect=[1])
    @patch('random.randint', return_value=1)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_guess_correctly(self, mock_stdout, _, __, ___):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.guessing_game(test_character)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = "A drow blocks your path!\n\n\nSuccess! You have slain the drow!\n\n"
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('game.pick_type_of_foe', return_value="drow")
    @patch('builtins.input', side_effect=[5])
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_guess_too_high(self, mock_stdout, _, __, ___):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.guessing_game(test_character)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = ("A drow blocks your path!\n\n\nOh no! You take 1 point of damage from "
                           "the drow!\n\n")
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('game.pick_type_of_foe', return_value="drow")
    @patch('builtins.input', side_effect=[1])
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_guess_too_low(self, mock_stdout, _, __, ___):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.guessing_game(test_character)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = ("A drow blocks your path!\n\n\nOh no! You take 1 point of damage from "
                           "the drow!\n\n")
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('game.pick_type_of_foe', return_value="drow")
    @patch('builtins.input', side_effect=[-1])
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_guess_out_of_range_low(self, mock_stdout, _, __, ___):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.guessing_game(test_character)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = ("A drow blocks your path!\n\n\nOh no! You take 1 point of damage from "
                           "the drow!\n\n")
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('game.pick_type_of_foe', return_value="drow")
    @patch('builtins.input', side_effect=[8])
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_guess_out_of_range_high(self, mock_stdout, _, __, ___):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.guessing_game(test_character)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = ("A drow blocks your path!\n\n\nOh no! You take 1 point of damage from "
                           "the drow!\n\n")
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('game.pick_type_of_foe', return_value="drow")
    @patch('builtins.input', side_effect=[8])
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_foe_begins_with_a_consonant(self, mock_stdout, _, __, ___):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.guessing_game(test_character)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = ("A drow blocks your path!\n\n\nOh no! You take 1 point of damage from "
                           "the drow!\n\n")
        self.assertEqual(expected_output, the_game_printed_this)

    @patch('game.pick_type_of_foe', return_value="intellect devourer")
    @patch('builtins.input', side_effect=[8])
    @patch('random.randint', return_value=3)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_guessing_game_foe_begins_with_a_vowel(self, mock_stdout, _, __, ___):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.guessing_game(test_character)
        the_game_printed_this = mock_stdout.getvalue()
        expected_output = ("An intellect devourer blocks your path!\n\n\nOh no! You take 1 point "
                           "of damage from the intellect devourer!\n\n")
        self.assertEqual(expected_output, the_game_printed_this)
