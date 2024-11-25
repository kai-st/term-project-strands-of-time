from unittest import TestCase

import character


class TestCreateCharacter(TestCase):

    def test_create_character_returns_dict(self):
        result = character.create_character()
        actual = type(result)
        expected = type({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5})
        self.assertEqual(expected, actual)

    def test_create_character_length(self):
        result = character.create_character()
        actual = len(result)
        expected = len({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5})
        self.assertEqual(expected, actual)

    def test_create_character_contains_x_coordinate_key(self):
        result = character.create_character()
        self.assertIn("X-coordinate", result)

    def test_create_character_contains_y_coordinate_key(self):
        result = character.create_character()
        self.assertIn("Y-coordinate", result)

    def test_create_character_contains_current_HP_key(self):
        result = character.create_character()
        self.assertIn("Current HP", result)

    def test_create_character_x_coordinate_value_is_0(self):
        result = character.create_character()
        actual = result["X-coordinate"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_create_character_y_coordinate_value_is_0(self):
        result = character.create_character()
        actual = result["Y-coordinate"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_create_character_current_HP_value_is_5(self):
        result = character.create_character()
        actual = result["Current HP"]
        expected = 5
        self.assertEqual(expected, actual)
