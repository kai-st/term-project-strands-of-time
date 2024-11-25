import io
from unittest import TestCase
from unittest.mock import patch

import strands_of_time.location.move
from strands_of_time import game


class TestGetUserChoice(TestCase):

    @patch('builtins.input', side_effect=["1"])
    def test_get_user_choice_north(self, _):
        actual = strands_of_time.location.move.get_move_from_player()
        expected = "north"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2"])
    def test_get_user_choice_south(self, _):
        actual = strands_of_time.location.move.get_move_from_player()
        expected = "south"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["3"])
    def test_get_user_choice_west(self, _):
        actual = strands_of_time.location.move.get_move_from_player()
        expected = "west"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["4"])
    def test_get_user_choice_east(self, _):
        actual = strands_of_time.location.move.get_move_from_player()
        expected = "east"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["5", "1"])
    def test_get_user_choice_invalid_numerical_entry(self, _, mock_stdout):
        strands_of_time.location.move.get_move_from_player()
        expected = "\nSorry, that is not a valid direction. Please try again.\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["w", "1"])
    def test_get_user_choice_invalid_alpha_entry(self, _, mock_stdout):
        strands_of_time.location.move.get_move_from_player()
        expected = "\nSorry, that is not a valid direction. Please try again.\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())
