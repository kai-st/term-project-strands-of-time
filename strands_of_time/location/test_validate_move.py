from unittest import TestCase

from strands_of_time.location import move


class TestValidateMove(TestCase):

    def test_validate_move_cannot_move_w_from_top_row(self):
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
        test_character = {"X-coordinate": 1, "Y-coordinate": 0}
        actual = move.validate_move(test_board, test_character, "w")
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_cannot_move_s_from_bottom_row(self):
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
        test_character = {"X-coordinate": 0, "Y-coordinate": 2}
        actual = move.validate_move(test_board, test_character, "s")
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_cannot_move_a_from_left_column(self):
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
        test_character = {"X-coordinate": 0, "Y-coordinate": 1}
        actual = move.validate_move(test_board, test_character, "a")
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_cannot_move_d_from_right_column(self):
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
        test_character = {"X-coordinate": 2, "Y-coordinate": 1}
        actual = move.validate_move(test_board, test_character, "d")
        expected = False
        self.assertEqual(expected, actual)

    def test_validate_move_can_move_s_from_top_row(self):
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
        test_character = {"X-coordinate": 1, "Y-coordinate": 0}
        actual = move.validate_move(test_board, test_character, "s")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_can_move_w_from_bottom_row(self):
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
        test_character = {"X-coordinate": 0, "Y-coordinate": 2}
        actual = move.validate_move(test_board, test_character, "w")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_can_move_d_from_left_column(self):
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
        test_character = {"X-coordinate": 0, "Y-coordinate": 1}
        actual = move.validate_move(test_board, test_character, "d")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_can_move_a_from_right_column(self):
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
        test_character = {"X-coordinate": 2, "Y-coordinate": 1}
        actual = move.validate_move(test_board, test_character, "a")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_can_move_s_from_center(self):
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
        test_character = {"X-coordinate": 1, "Y-coordinate": 1}
        actual = move.validate_move(test_board, test_character, "s")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_can_move_w_from_center(self):
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
        test_character = {"X-coordinate": 1, "Y-coordinate": 1}
        actual = move.validate_move(test_board, test_character, "w")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_can_move_d_from_center(self):
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
        test_character = {"X-coordinate": 1, "Y-coordinate": 1}
        actual = move.validate_move(test_board, test_character, "d")
        expected = True
        self.assertEqual(expected, actual)

    def test_validate_move_can_move_a_from_center(self):
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
        test_character = {"X-coordinate": 1, "Y-coordinate": 1}
        actual = move.validate_move(test_board, test_character, "a")
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
        test_character = {"X-coordinate": 1, "Y-coordinate": 1}
        move.validate_move(test_board, test_character, "a")
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
        test_character = {"X-coordinate": 1, "Y-coordinate": 1}
        move.validate_move(test_board, test_character, "w")
        actual = test_character["Y-coordinate"]
        expected = 1
        self.assertEqual(expected, actual)
