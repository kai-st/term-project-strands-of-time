import io
from unittest import TestCase
from unittest.mock import patch

from strands_of_time import game


class TestDisplayGameState(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_game_state_smallest_board_initial_state(self, mock_stdout):
        test_board = {(0, 0): "room description"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        game.show_game_state(test_board, test_character)
        expected = ("\n--- Current HP: 5 --- Current location: Row 1, Column 1 --- Goal: Row 1, "
                    "Column 1 ---\n\n")
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_game_state_board_2_by_2_initial_state(self, mock_stdout):
        test_board = {(0, 0): "room description",
                      (1, 0): "room description",
                      (0, 1): "room description",
                      (1, 1): "room description"
                      }
        test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        game.show_game_state(test_board, test_character)
        expected = ("\n--- Current HP: 5 --- Current location: Row 1, Column 1 --- Goal: Row 2, "
                    "Column 2 ---\n\n")
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_game_state_hp_3(self, mock_stdout):
        test_board = {(0, 0): "room description",
                      (1, 0): "room description",
                      (0, 1): "room description",
                      (1, 1): "room description"
                      }
        test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 3}
        game.show_game_state(test_board, test_character)
        expected = ("\n--- Current HP: 3 --- Current location: Row 1, Column 1 --- Goal: Row 2, "
                    "Column 2 ---\n\n")
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_game_state_character_location_x_1(self, mock_stdout):
        test_board = {(0, 0): "room description",
                      (1, 0): "room description",
                      (0, 1): "room description",
                      (1, 1): "room description"
                      }
        test_character = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 3}
        game.show_game_state(test_board, test_character)
        expected = ("\n--- Current HP: 3 --- Current location: Row 1, Column 2 --- Goal: Row 2, "
                    "Column 2 ---\n\n")
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_display_game_state_character_location_y_1(self, mock_stdout):
        test_board = {(0, 0): "room description",
                      (1, 0): "room description",
                      (0, 1): "room description",
                      (1, 1): "room description"
                      }
        test_character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 3}
        game.show_game_state(test_board, test_character)
        expected = ("\n--- Current HP: 3 --- Current location: Row 2, Column 1 --- Goal: Row 2, "
                    "Column 2 ---\n\n")
        self.assertEqual(expected, mock_stdout.getvalue())
