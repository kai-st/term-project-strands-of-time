from unittest import TestCase


import game


class TestPrepGoalForPrinting(TestCase):

    def test_prep_goal_for_printing_smallest_board(self):
        test_board = {(0, 0): "room description"}
        actual = game.prep_goal_for_printing(test_board)
        expected = "Goal: Row 1, Column 1"
        self.assertEqual(expected, actual)

    def test_prep_goal_for_printing_2_rooms(self):
        test_board = {(0, 0): "room description", (1, 0): "room description"}
        actual = game.prep_goal_for_printing(test_board)
        expected = "Goal: Row 1, Column 2"
        self.assertEqual(expected, actual)

    def test_prep_goal_for_printing_board_2_by_2(self):
        test_board = {(0, 0): "room description",
                    (1, 0): "room description",
                    (0, 1): "room description",
                    (1, 1): "room description"
                    }
        actual = game.prep_goal_for_printing(test_board)
        expected = "Goal: Row 2, Column 2"
        self.assertEqual(expected, actual)

    def test_prep_goal_for_printing_board_not_square(self):
        test_board = {(0, 0): "room description",
                      (0, 1): "room description",
                      (1, 0): "room description",
                      (1, 1): "room description",
                      (2, 0): "room description",
                      (2, 1): "room description"
                      }
        actual = game.prep_goal_for_printing(test_board)
        expected = "Goal: Row 2, Column 3"
        self.assertEqual(expected, actual)
