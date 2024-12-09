from unittest import TestCase

from strands_of_time.character import character


class TestCreateCharacter(TestCase):

    def test_create_character_returns_dict(self):
        result = character.create_character(3)
        actual = type(result)
        expected = type({"X-coordinate": -1,
                         "Y-coordinate": -1,
                         "level": 1,
                         "last distance to goal": None,
                         "Strands": {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3,
                                     "Blue": 3, "Violet": 3}})
        self.assertEqual(expected, actual)

    def test_create_character_length(self):
        result = character.create_character(3)
        actual = len(result)
        expected = len({"X-coordinate": -1,
                        "Y-coordinate": -1,
                        "level": 1,
                        "last distance to goal": None,
                        "Strands": {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3,
                                    "Blue": 3, "Violet": 3}})
        self.assertEqual(expected, actual)

    def test_create_character_contains_x_coordinate_key(self):
        result = character.create_character(3)
        self.assertIn("X-coordinate", result)

    def test_create_character_contains_y_coordinate_key(self):
        result = character.create_character(3)
        self.assertIn("Y-coordinate", result)

    def test_create_character_contains_level_key(self):
        result = character.create_character(3)
        self.assertIn("level", result)

    def test_create_character_contains_last_distance_to_goal_key(self):
        result = character.create_character(3)
        self.assertIn("last distance to goal", result)

    def test_create_character_contains_strands_key(self):
        result = character.create_character(3)
        self.assertIn("Strands", result)

    def test_create_character_x_coordinate_value_is_neg_1(self):
        result = character.create_character(3)
        actual = result["X-coordinate"]
        expected = -1
        self.assertEqual(expected, actual)

    def test_create_character_y_coordinate_value_is_neg_1(self):
        result = character.create_character(3)
        actual = result["Y-coordinate"]
        expected = -1
        self.assertEqual(expected, actual)

    def test_create_character_level_is_1(self):
        result = character.create_character(3)
        actual = result["level"]
        expected = 1
        self.assertEqual(expected, actual)

    def test_create_character_last_distance_to_goal_is_None(self):
        result = character.create_character(3)
        actual = result["last distance to goal"]
        expected = None
        self.assertEqual(expected, actual)

    def test_create_character_strands_is_dict(self):
        result = character.create_character(3)
        actual = type(result["Strands"])
        expected = type({"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3, "Blue": 3, "Violet": 3})
        self.assertEqual(expected, actual)

    def test_create_character_strands_has_all_colours_at_3(self):
        result = character.create_character(3)
        actual = result["Strands"]
        expected = {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3, "Blue": 3, "Violet": 3}
        self.assertEqual(expected, actual)

    def test_create_character_strands_has_all_colours_at_0(self):
        result = character.create_character(0)
        actual = result["Strands"]
        expected = {"Red": 0, "Orange": 0, "Yellow": 0, "Green": 0, "Blue": 0, "Violet": 0}
        self.assertEqual(expected, actual)

    def test_create_character_strands_has_all_colours_at_10(self):
        result = character.create_character(10)
        actual = result["Strands"]
        expected = {"Red": 10, "Orange": 10, "Yellow": 10, "Green": 10, "Blue": 10, "Violet": 10}
        self.assertEqual(expected, actual)

    def test_create_character_raises_value_error_on_negative_initial_strands(self):
        with self.assertRaises(ValueError):
            character.create_character(-1)

    def test_create_character_raises_type_error_if_initial_strands_not_int(self):
        with self.assertRaises(TypeError):
            character.create_character("3")
