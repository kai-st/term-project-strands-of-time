import io
from unittest import TestCase
from unittest.mock import patch


import game


class TestGetUserChoice(TestCase):

    @patch('builtins.input', side_effect=["1"])
    def test_get_user_choice_north(self, _):
        actual = game.get_user_choice()
        expected = "north"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2"])
    def test_get_user_choice_south(self, _):
        actual = game.get_user_choice()
        expected = "south"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["3"])
    def test_get_user_choice_west(self, _):
        actual = game.get_user_choice()
        expected = "west"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["4"])
    def test_get_user_choice_east(self, _):
        actual = game.get_user_choice()
        expected = "east"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["5", "1"])
    def test_get_user_choice_invalid_numerical_entry(self, _, mock_stdout):
        game.get_user_choice()
        expected = "\nSorry, that is not a valid direction. Please try again.\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["w", "1"])
    def test_get_user_choice_invalid_alpha_entry(self, _, mock_stdout):
        game.get_user_choice()
        expected = "\nSorry, that is not a valid direction. Please try again.\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())
