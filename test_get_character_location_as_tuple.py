from unittest import TestCase

import game


class TestGetCharacterLocationAsTuple(TestCase):

    def test_get_character_location_as_tuple_returns_tuple(self):
        test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        actual = type(game.get_character_location_as_tuple(test_character))
        expected = type((0, 0))
        self.assertEqual(expected, actual)

    def test_get_character_location_as_tuple_X_at_index_0(self):
        test_character = {"X-coordinate": 2, "Y-coordinate": 4, "Current HP": 5}
        location = game.get_character_location_as_tuple(test_character)
        actual = location[0]
        expected = test_character["X-coordinate"]
        self.assertEqual(expected, actual)

    def test_get_character_location_as_tuple_Y_at_index_1(self):
        test_character = {"X-coordinate": 2, "Y-coordinate": 4, "Current HP": 5}
        location = game.get_character_location_as_tuple(test_character)
        actual = location[1]
        expected = test_character["Y-coordinate"]
        self.assertEqual(expected, actual)

    def test_get_character_location_as_tuple_initial_location(self):
        test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        actual = game.get_character_location_as_tuple(test_character)
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_get_character_location_as_tuple_goal_location(self):
        test_character = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 5}
        actual = game.get_character_location_as_tuple(test_character)
        expected = (4, 4)
        self.assertEqual(expected, actual)

    def test_get_character_location_as_tuple_location_X_2_Y_3(self):
        test_character = {"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 5}
        actual = game.get_character_location_as_tuple(test_character)
        expected = (2, 3)
        self.assertEqual(expected, actual)
