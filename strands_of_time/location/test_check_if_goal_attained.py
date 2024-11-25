from unittest import TestCase

from strands_of_time import game


class TestCheckIfGoalAttained(TestCase):

    def test_check_if_goal_attained_initial_location(self):
        test_board = {(0, 0): "room description A",
                      (1, 0): "room description B",
                      (0, 1): "room description C",
                      (1, 1): "room description D"
                      }
        test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        actual = game.check_if_goal_attained(test_board, test_character)
        expected = False
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_central_location(self):
        test_board = {(0, 0): "room description A",
                      (1, 0): "room description B",
                      (0, 1): "room description C",
                      (1, 1): "room description D"
                      }
        test_character = {"X-coordinate": 0, "Y-coordinate": 1, "Current HP": 5}
        actual = game.check_if_goal_attained(test_board, test_character)
        expected = False
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_final_location(self):
        test_board = {(0, 0): "room description A",
                      (1, 0): "room description B",
                      (0, 1): "room description C",
                      (1, 1): "room description D"
                      }
        test_character = {"X-coordinate": 1, "Y-coordinate": 1, "Current HP": 5}
        actual = game.check_if_goal_attained(test_board, test_character)
        expected = True
        self.assertEqual(expected, actual)

    def test_check_if_goal_attained_initial_location_smallest_board(self):
        test_board = {(0, 0): "room description A"}
        test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        actual = game.check_if_goal_attained(test_board, test_character)
        expected = True
        self.assertEqual(expected, actual)
