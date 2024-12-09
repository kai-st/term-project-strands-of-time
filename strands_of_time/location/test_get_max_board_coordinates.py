from unittest import TestCase


from strands_of_time.location import board


class TestGetMaxBoardCoordinates(TestCase):

    def test_get_max_board_coordinates_returns_tuple(self):
        test_board = {(0, 0): {"description": "room description"}}
        actual = type(board.get_max_board_coordinates(test_board))
        expected = type((0, 0))
        self.assertEqual(expected, actual)

    def test_get_max_board_coordinates_x_coordinate_at_index_0(self):
        test_board = {(0, 0): {"description": "room description"}, (1, 0): {"description": ("room "
                                                                                  "description")}}
        location = board.get_max_board_coordinates(test_board)
        actual = location[0]
        expected = 1
        self.assertEqual(expected, actual)

    def test_get_max_board_coordinates_y_coordinate_at_index_1(self):
        test_board = {(0, 0): {"description": "room description"}, (1, 0): {"description": ("room "
                                                                                  "description")}}
        location = board.get_max_board_coordinates(test_board)
        actual = location[1]
        expected = 0
        self.assertEqual(expected, actual)

    def test_get_max_board_coordinates_smallest_board(self):
        test_board = {(0, 0): {"description": "room description"}}
        actual = board.get_max_board_coordinates(test_board)
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_get_max_board_coordinates_2_rooms(self):
        test_board = {(0, 0): {"description": "room description"}, (1, 0): {"description": ("room "
                                                                                  "description")}}
        actual = board.get_max_board_coordinates(test_board)
        expected = (1, 0)
        self.assertEqual(expected, actual)

    def test_get_max_board_coordinates_board_2_by_2(self):
        test_board = {(0, 0): {"description": "room description"},
                    (1, 0): {"description": "room description"},
                    (0, 1): {"description": "room description"},
                    (1, 1): {"description": "room description"}
                    }
        actual = board.get_max_board_coordinates(test_board)
        expected = (1, 1)
        self.assertEqual(expected, actual)

    def test_get_max_board_coordinates_board_not_square(self):
        test_board = {(0, 0): {"description": "room description"},
                      (0, 1): {"description": "room description"},
                      (1, 0): {"description": "room description"},
                      (1, 1): {"description": "room description"},
                      (2, 0): {"description": "room description"},
                      (2, 1): {"description": "room description"}
                      }
        actual = board.get_max_board_coordinates(test_board)
        expected = (2, 1)
        self.assertEqual(expected, actual)
