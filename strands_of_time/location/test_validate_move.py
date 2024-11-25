from unittest import TestCase

import strands_of_time.location.move
from strands_of_time import game


class TestValidateMove(TestCase):

    def test_validate_move_cannot_move_north_from_top_row(self):
        test_board = {(0, 0): "room description",
                      (0, 1): "room description",
                      (0, 2): "room description",
                      (1, 0): "room description",
                      (1, 1): "room description",
                      (1, 2): "room description",
                      (2, 0): "room description",
                      (2, 1): "room description",
                      (2, 2): "room description"
                      }
        test_character = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5}
        actual = strands_of_time.location.move.validate_move(test_board, test_character, "north")
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_cannot_move_south_from_bottom_row(self):
        test_board = {(0, 0): "room description",
                      (0, 1): "room description",
                      (0, 2): "room description",
                      (1, 0): "room description",
                      (1, 1): "room description",
                      (1, 2): "room description",
                      (2, 0): "room description",
                      (2, 1): "room description",
                      (2, 2): "room description"
                      }
        test_character = {"X-coordinate": 0, "Y-coordinate": 2, "Current HP": 5}
        actual = strands_of_time.location.move.validate_move(test_board, test_character, "south")
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_cannot_move_west_from_left_column(self):
        test_board = {(0, 0): "room description",
                      (0, 1): "room description",
                      (0, 2): "room description",
                      (1, 0): "room description",
                      (1, 1): "room description",
                      (1, 2): "room description",
                      (2, 0): "room description",
                      (2, 1): "room description",
                      (2, 2): "room description"
                      }
        test_character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        actual = strands_of_time.location.move.validate_move(test_board, test_character, "west")
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_cannot_move_east_from_right_column(self):
        test_board = {(0, 0): "room description",
                      (0, 1): "room description",
                      (0, 2): "room description",
                      (1, 0): "room description",
                      (1, 1): "room description",
                      (1, 2): "room description",
                      (2, 0): "room description",
                      (2, 1): "room description",
                      (2, 2): "room description"
                      }
        test_character = {"X-coordinate": 2, "Y-coordinate": 1, "Current HP": 5}
        actual = strands_of_time.location.move.validate_move(test_board, test_character, "east")
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_can_move_south_from_top_row(self):
        test_board = {(0, 0): "room description",
                      (0, 1): "room description",
                      (0, 2): "room description",
                      (1, 0): "room description",
                      (1, 1): "room description",
                      (1, 2): "room description",
                      (2, 0): "room description",
                      (2, 1): "room description",
                      (2, 2): "room description"
                      }
        test_character = {"X-coordinate": 1, "Y-coordinate": 0, "Current HP": 5}
        actual = strands_of_time.location.move.validate_move(test_board, test_character, "south")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_can_move_north_from_bottom_row(self):
        test_board = {(0, 0): "room description",
                      (0, 1): "room description",
                      (0, 2): "room description",
                      (1, 0): "room description",
                      (1, 1): "room description",
                      (1, 2): "room description",
                      (2, 0): "room description",
                      (2, 1): "room description",
                      (2, 2): "room description"
                      }
        test_character = {"X-coordinate": 0, "Y-coordinate": 2, "Current HP": 5}
        actual = strands_of_time.location.move.validate_move(test_board, test_character, "north")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_can_move_east_from_left_column(self):
        test_board = {(0, 0): "room description",
                      (0, 1): "room description",
                      (0, 2): "room description",
                      (1, 0): "room description",
                      (1, 1): "room description",
                      (1, 2): "room description",
                      (2, 0): "room description",
                      (2, 1): "room description",
                      (2, 2): "room description"
                      }
        test_character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        actual = strands_of_time.location.move.validate_move(test_board, test_character, "east")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_can_move_west_from_right_column(self):
        test_board = {(0, 0): "room description",
                      (0, 1): "room description",
                      (0, 2): "room description",
                      (1, 0): "room description",
                      (1, 1): "room description",
                      (1, 2): "room description",
                      (2, 0): "room description",
                      (2, 1): "room description",
                      (2, 2): "room description"
                      }
        test_character = {"X-coordinate": 2, "Y-coordinate": 1, "Current HP": 5}
        actual = strands_of_time.location.move.validate_move(test_board, test_character, "west")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_can_move_south_from_center(self):
        test_board = {(0, 0): "room description",
                      (0, 1): "room description",
                      (0, 2): "room description",
                      (1, 0): "room description",
                      (1, 1): "room description",
                      (1, 2): "room description",
                      (2, 0): "room description",
                      (2, 1): "room description",
                      (2, 2): "room description"
                      }
        test_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        actual = strands_of_time.location.move.validate_move(test_board, test_character, "south")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_can_move_north_from_center(self):
        test_board = {(0, 0): "room description",
                      (0, 1): "room description",
                      (0, 2): "room description",
                      (1, 0): "room description",
                      (1, 1): "room description",
                      (1, 2): "room description",
                      (2, 0): "room description",
                      (2, 1): "room description",
                      (2, 2): "room description"
                      }
        test_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        actual = strands_of_time.location.move.validate_move(test_board, test_character, "north")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_can_move_east_from_center(self):
        test_board = {(0, 0): "room description",
                      (0, 1): "room description",
                      (0, 2): "room description",
                      (1, 0): "room description",
                      (1, 1): "room description",
                      (1, 2): "room description",
                      (2, 0): "room description",
                      (2, 1): "room description",
                      (2, 2): "room description"
                      }
        test_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        actual = strands_of_time.location.move.validate_move(test_board, test_character, "east")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_can_move_west_from_center(self):
        test_board = {(0, 0): "room description",
                      (0, 1): "room description",
                      (0, 2): "room description",
                      (1, 0): "room description",
                      (1, 1): "room description",
                      (1, 2): "room description",
                      (2, 0): "room description",
                      (2, 1): "room description",
                      (2, 2): "room description"
                      }
        test_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        actual = strands_of_time.location.move.validate_move(test_board, test_character, "west")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_character_x_coordinate_unchanged(self):
        test_board = {(0, 0): "room description",
                      (0, 1): "room description",
                      (0, 2): "room description",
                      (1, 0): "room description",
                      (1, 1): "room description",
                      (1, 2): "room description",
                      (2, 0): "room description",
                      (2, 1): "room description",
                      (2, 2): "room description"
                      }
        test_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        strands_of_time.location.move.validate_move(test_board, test_character, "west")
        actual = test_character["X-coordinate"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_validate_move_character_y_coordinate_unchanged(self):
        test_board = {(0, 0): "room description",
                      (0, 1): "room description",
                      (0, 2): "room description",
                      (1, 0): "room description",
                      (1, 1): "room description",
                      (1, 2): "room description",
                      (2, 0): "room description",
                      (2, 1): "room description",
                      (2, 2): "room description"
                      }
        test_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        strands_of_time.location.move.validate_move(test_board, test_character, "north")
        actual = test_character["Y-coordinate"]
        expected = 1
        self.assertEqual(expected, actual)
