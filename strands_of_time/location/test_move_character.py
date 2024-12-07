from unittest import TestCase

import move


class TestMoveCharacter(TestCase):

    def test_move_character_w_decrements_y(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "level": 2}
        move.move_character(test_character, "w")
        actual = test_character["Y-coordinate"]
        expected = 2
        self.assertEqual(expected, actual)

    def test_move_character_w_does_not_change_x(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "level": 2}
        move.move_character(test_character, "w")
        actual = test_character["X-coordinate"]
        expected = 3
        self.assertEqual(expected, actual)

    def test_move_character_w_does_not_change_level(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "level": 2}
        move.move_character(test_character, "w")
        actual = test_character["level"]
        expected = 2
        self.assertEqual(expected, actual)

    def test_move_character_s_increments_y(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "level": 2}
        move.move_character(test_character, "s")
        actual = test_character["Y-coordinate"]
        expected = 4
        self.assertEqual(expected, actual)

    def test_move_character_s_does_not_change_x(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "level": 2}
        move.move_character(test_character, "s")
        actual = test_character["X-coordinate"]
        expected = 3
        self.assertEqual(expected, actual)

    def test_move_character_s_does_not_change_level(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "level": 2}
        move.move_character(test_character, "s")
        actual = test_character["level"]
        expected = 2
        self.assertEqual(expected, actual)

    def test_move_character_a_decrements_x(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "level": 2}
        move.move_character(test_character, "a")
        actual = test_character["X-coordinate"]
        expected = 2
        self.assertEqual(expected, actual)

    def test_move_character_a_does_not_change_y(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "level": 2}
        move.move_character(test_character, "a")
        actual = test_character["Y-coordinate"]
        expected = 3
        self.assertEqual(expected, actual)

    def test_move_character_a_does_not_change_level(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "level": 2}
        move.move_character(test_character, "a")
        actual = test_character["level"]
        expected = 2
        self.assertEqual(expected, actual)

    def test_move_character_d_increments_x(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "level": 2}
        move.move_character(test_character, "d")
        actual = test_character["X-coordinate"]
        expected = 4
        self.assertEqual(expected, actual)

    def test_move_character_d_does_not_change_y(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "level": 2}
        move.move_character(test_character, "d")
        actual = test_character["Y-coordinate"]
        expected = 3
        self.assertEqual(expected, actual)

    def test_move_character_d_does_not_change_level(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "level": 2}
        move.move_character(test_character, "d")
        actual = test_character["level"]
        expected = 2
        self.assertEqual(expected, actual)

    def test_move_character_jump_does_not_change_level(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "level": 2}
        move.move_character(test_character, "4d2s")
        actual = test_character["level"]
        expected = 2
        self.assertEqual(expected, actual)

    def test_move_character_jump_increments_x(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "level": 2}
        move.move_character(test_character, "4d2s")
        actual = test_character["X-coordinate"]
        expected = 7
        self.assertEqual(expected, actual)


    def test_move_character_jump_increments_y(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "level": 2}
        move.move_character(test_character, "4d2s")
        actual = test_character["Y-coordinate"]
        expected = 5
        self.assertEqual(expected, actual)

    def test_move_character_jump_decrements_x(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "level": 2}
        move.move_character(test_character, "2a2s")
        actual = test_character["X-coordinate"]
        expected = 1
        self.assertEqual(expected, actual)


    def test_move_character_jump_decrements_y(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "level": 2}
        move.move_character(test_character, "4d2w")
        actual = test_character["Y-coordinate"]
        expected = 1
        self.assertEqual(expected, actual)
