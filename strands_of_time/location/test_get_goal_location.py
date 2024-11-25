from unittest import TestCase

from strands_of_time import game


class TestGetGoalLocation(TestCase):

    def test_get_goal_location_returns_tuple(self):
        test_board = {(0, 0): "room description"}
        actual = type(game.get_goal_location(test_board))
        expected = type((0, 0))
        self.assertEqual(expected, actual)

    def test_get_goal_location_x_coordinate_at_index_0(self):
        test_board = {(0, 0): "room description", (1, 0): "room description"}
        location = game.get_goal_location(test_board)
        actual = location[0]
        expected = 1
        self.assertEqual(expected, actual)

    def test_get_goal_location_y_coordinate_at_index_1(self):
        test_board = {(0, 0): "room description", (1, 0): "room description"}
        location = game.get_goal_location(test_board)
        actual = location[1]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_goal_location_smallest_board(self):
        test_board = {(0, 0): "room description"}
        actual = game.get_goal_location(test_board)
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_get_goal_location_2_rooms(self):
        test_board = {(0, 0): "room description", (1, 0): "room description"}
        actual = game.get_goal_location(test_board)
        expected = (1, 0)
        self.assertEqual(expected, actual)

    def test_get_goal_location_board_2_by_2(self):
        test_board = {(0, 0): "room description",
                    (1, 0): "room description",
                    (0, 1): "room description",
                    (1, 1): "room description"
                    }
        actual = game.get_goal_location(test_board)
        expected = (1, 1)
        self.assertEqual(expected, actual)

    def test_get_goal_location_board_not_square(self):
        test_board = {(0, 0): "room description",
                      (0, 1): "room description",
                      (1, 0): "room description",
                      (1, 1): "room description",
                      (2, 0): "room description",
                      (2, 1): "room description"
                      }
        actual = game.get_goal_location(test_board)
        expected = (2, 1)
        self.assertEqual(expected, actual)
