from unittest import TestCase
from unittest.mock import patch

import strands_of_time.location.board
from strands_of_time import game


class TestMakeBoard(TestCase):

    def test_make_board_smallest_board(self):
        actual = strands_of_time.location.board.create_game_board(1, 1)
        expected = {(0, 0): "a dark cavern at the northwest end of a tangled cave system deep in "
                            "the Underdark with\nonly the dim glow of your trusty magic blade to "
                            "lead you to the surface."}
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=["room description", "room description"])
    def test_make_board_2_x_2(self, _):
        actual = strands_of_time.location.board.create_game_board(2, 2)
        expected = {(0, 0): "a dark cavern at the northwest end of a tangled cave system deep in "
                            "the Underdark with\nonly the dim glow of your trusty magic blade to "
                            "lead you to the surface.",
                    (1, 0): "room description",
                    (0, 1): "room description",
                    (1, 1): "a narrow tunnel. Finally, you can see the glimmer of surface sunlight "
                            "filtering into\nthe mouth of the cave ahead of you."
                    }
        self.assertEqual(expected, actual)

    @patch('random.choice', side_effect=["room description", "room description",
                                         "room description", "room description"])
    def test_make_board_not_square(self, _):
        actual = strands_of_time.location.board.create_game_board(2, 3)
        expected = {(0, 0): "a dark cavern at the northwest end of a tangled cave system deep in "
                            "the Underdark with\nonly the dim glow of your trusty magic blade to "
                            "lead you to the surface.",
                    (0, 1): "room description",
                    (1, 0): "room description",
                    (1, 1): "room description",
                    (2, 0): "room description",
                    (2, 1): "a narrow tunnel. Finally, you can see the glimmer of surface sunlight "
                            "filtering into\nthe mouth of the cave ahead of you."
                    }
        self.assertEqual(expected, actual)

    def test_make_board_large_board(self):
        actual = len(strands_of_time.location.board.create_game_board(10, 10))
        expected = 10 * 10
        self.assertEqual(expected, actual)

    def test_make_board_huge_board(self):
        actual = len(strands_of_time.location.board.create_game_board(100, 100))
        expected = 100 * 100
        self.assertEqual(expected, actual)

    def test_make_board_returns_dict(self):
        actual = type(strands_of_time.location.board.create_game_board(1, 1))
        expected = type({(0, 0): "room description"})
        self.assertEqual(expected, actual)
