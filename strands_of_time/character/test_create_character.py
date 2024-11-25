from unittest import TestCase

import character


class TestCreateCharacter(TestCase):

    def test_create_character_returns_dict(self):
        result = character.create_character()
        actual = type(result)
        expected = type({"X-coordinate": -1,
                         "Y-coordinate": -1,
                         "level": 1,
                         "last distance to goal": None,
                         "Strands": {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3,
                                     "Blue": 3, "Violet": 3}})
        self.assertEqual(expected, actual)

    def test_create_character_length(self):
        result = character.create_character()
        actual = len(result)
        expected = len({"X-coordinate": -1,
                        "Y-coordinate": -1,
                        "level": 1,
                        "last distance to goal": None,
                        "Strands": {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3,
                                    "Blue": 3, "Violet": 3}})
        self.assertEqual(expected, actual)

    def test_create_character_contains_x_coordinate_key(self):
        result = character.create_character()
        self.assertIn("X-coordinate", result)

    def test_create_character_contains_y_coordinate_key(self):
        result = character.create_character()
        self.assertIn("Y-coordinate", result)

    def test_create_character_contains_level_key(self):
        result = character.create_character()
        self.assertIn("level", result)

    def test_create_character_contains_last_distance_to_goal_key(self):
        result = character.create_character()
        self.assertIn("last distance to goal", result)

    def test_create_character_contains_strands_key(self):
        result = character.create_character()
        self.assertIn("Strands", result)

    def test_create_character_x_coordinate_value_is_neg_1(self):
        result = character.create_character()
        actual = result["X-coordinate"]
        expected = -1
        self.assertEqual(expected, actual)

    def test_create_character_y_coordinate_value_is_neg_1(self):
        result = character.create_character()
        actual = result["Y-coordinate"]
        expected = -1
        self.assertEqual(expected, actual)

    def test_create_character_level_is_1(self):
        result = character.create_character()
        actual = result["level"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_create_character_last_distance_to_goal_is_None(self):
        result = character.create_character()
        actual = result["last distance to goal"]
        expected = None
        self.assertEqual(expected, actual)

    def test_create_character_strands_is_dict(self):
        result = character.create_character()
        actual = type(result["Strands"])
        expected = type({"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3, "Blue": 3, "Violet": 3})
        self.assertEqual(expected, actual)

    def test_create_character_strands_has_all_colours_at_3(self):
        result = character.create_character()
        actual = result["Strands"]
        expected = {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3, "Blue": 3, "Violet": 3}
        self.assertEqual(expected, actual)
