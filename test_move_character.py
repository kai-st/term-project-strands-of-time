from unittest import TestCase


import game


class TestMoveCharacter(TestCase):

    def test_move_character_north_decrements_y(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.move_character(test_character, "north")
        actual = test_character["Y-coordinate"]
        expected = 2
        self.assertEqual(expected, actual)

    def test_move_character_north_does_not_change_x(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.move_character(test_character, "north")
        actual = test_character["X-coordinate"]
        expected = 3
        self.assertEqual(expected, actual)

    def test_move_character_north_does_not_change_hp(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.move_character(test_character, "north")
        actual = test_character["Current HP"]
        expected = 5
        self.assertEqual(expected, actual)

    def test_move_character_south_increments_y(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.move_character(test_character, "south")
        actual = test_character["Y-coordinate"]
        expected = 4
        self.assertEqual(expected, actual)

    def test_move_character_south_does_not_change_x(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.move_character(test_character, "south")
        actual = test_character["X-coordinate"]
        expected = 3
        self.assertEqual(expected, actual)

    def test_move_character_south_does_not_change_hp(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.move_character(test_character, "south")
        actual = test_character["Current HP"]
        expected = 5
        self.assertEqual(expected, actual)

    def test_move_character_west_decrements_x(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.move_character(test_character, "west")
        actual = test_character["X-coordinate"]
        expected = 2
        self.assertEqual(expected, actual)

    def test_move_character_west_does_not_change_y(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.move_character(test_character, "west")
        actual = test_character["Y-coordinate"]
        expected = 3
        self.assertEqual(expected, actual)

    def test_move_character_west_does_not_change_hp(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.move_character(test_character, "west")
        actual = test_character["Current HP"]
        expected = 5
        self.assertEqual(expected, actual)

    def test_move_character_east_increments_x(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.move_character(test_character, "east")
        actual = test_character["X-coordinate"]
        expected = 4
        self.assertEqual(expected, actual)

    def test_move_character_east_does_not_change_y(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.move_character(test_character, "east")
        actual = test_character["Y-coordinate"]
        expected = 3
        self.assertEqual(expected, actual)

    def test_move_character_east_does_not_change_hp(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        game.move_character(test_character, "east")
        actual = test_character["Current HP"]
        expected = 5
        self.assertEqual(expected, actual)
