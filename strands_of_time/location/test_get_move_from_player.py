import io
from unittest import TestCase
from unittest.mock import patch


import move


class TestGetMoveFromPlayer(TestCase):

    @patch('builtins.input', side_effect=["1"])
    def test_get_move_from_player_north(self, _):
        actual = move.get_move_from_player()
        expected = "north"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2"])
    def test_get_move_from_player_south(self, _):
        actual = move.get_move_from_player()
        expected = "south"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["3"])
    def test_get_move_from_player_west(self, _):
        actual = move.get_move_from_player()
        expected = "west"
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["4"])
    def test_get_move_from_player_east(self, _):
        actual = move.get_move_from_player()
        expected = "east"
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["5", "1"])
    def test_get_move_from_player_invalid_numerical_entry(self, _, mock_stdout):
        move.get_move_from_player()
        expected = "\nSorry, that is not a valid direction. Please try again.\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    @patch('builtins.input', side_effect=["w", "1"])
    def test_get_move_from_player_invalid_alpha_entry(self, _, mock_stdout):
        move.get_move_from_player()
        expected = "\nSorry, that is not a valid direction. Please try again.\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())