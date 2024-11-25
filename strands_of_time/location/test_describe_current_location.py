import io
from unittest import TestCase
from unittest.mock import patch

import game

import strands_of_time.location.board


class TestDescribeCurrentLocation(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_initial_location(self, mock_stdout):
        test_board = {(0, 0): "room description A",
                      (1, 0): "room description B",
                      (0, 1): "room description C",
                      (1, 1): "room description D"
                      }
        test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        strands_of_time.location.board.describe_current_location(test_board, test_character)
        expected = "You're in room description A\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_final_room(self, mock_stdout):
        test_board = {(0, 0): "room description A",
                      (1, 0): "room description B",
                      (0, 1): "room description C",
                      (1, 1): "room description D"
                      }
        test_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        strands_of_time.location.board.describe_current_location(test_board, test_character)
        expected = "You're in room description D\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_describe_current_location_third_room(self, mock_stdout):
        test_board = {(0, 0): "room description A",
                      (1, 0): "room description B",
                      (0, 1): "room description C",
                      (1, 1): "room description D"
                      }
        test_character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        strands_of_time.location.board.describe_current_location(test_board, test_character)
        expected = "You're in room description C\n\n"
        self.assertEqual(expected, mock_stdout.getvalue())
