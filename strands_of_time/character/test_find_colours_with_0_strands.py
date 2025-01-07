from unittest import TestCase

from strands_of_time.character import character


class TestFindColoursWith0Strands(TestCase):

    def test_find_colours_with_0_strands_returns_list(self):
        actual = character.find_colours_with_0_strands({"X-coordinate": -1,
                                                        "Y-coordinate": -1,
                                                        "level": 1,
                                                        "last distance to goal": None,
                                                        "Strands": {"Red": 3, "Orange": 3,
                                                                    "Yellow": 3,
                                                                    "Green": 3,
                                                                    "Blue": 3, "Violet": 3}})
        self.assertIsInstance(actual, list)


    def test_find_colours_with_0_strands_returns_list_of_strings(self):
        actual = character.find_colours_with_0_strands({"X-coordinate": -1,
                                                        "Y-coordinate": -1,
                                                        "level": 1,
                                                        "last distance to goal": None,
                                                        "Strands": {"Red": 0, "Orange": 3,
                                                                    "Yellow": 3,
                                                                    "Green": 3,
                                                                    "Blue": 3, "Violet": 3}})
        self.assertIsInstance(actual[0], str)


    def test_find_colours_with_0_strands_initial_strands(self):
        actual = character.find_colours_with_0_strands({"X-coordinate": -1,
                                                        "Y-coordinate": -1,
                                                        "level": 1,
                                                        "last distance to goal": None,
                                                        "Strands": {"Red": 3, "Orange": 3,
                                                                    "Yellow": 3,
                                                                    "Green": 3,
                                                                    "Blue": 3, "Violet": 3}})
        expected = []
        self.assertEqual(expected, actual)


    def test_find_colours_with_0_strands_strands_can_be_floats(self):
        actual = character.find_colours_with_0_strands({"X-coordinate": -1,
                                                        "Y-coordinate": -1,
                                                        "level": 1,
                                                        "last distance to goal": None,
                                                        "Strands": {"Red": 3.5, "Orange": 3.5,
                                                                    "Yellow": 3.5,
                                                                    "Green": 3.5,
                                                                    "Blue": 3.5, "Violet": 3.5}})
        expected = []
        self.assertEqual(expected, actual)


    def test_find_colours_with_0_strands_strands_can_mix_ints_and_floats(self):
        actual = character.find_colours_with_0_strands({"X-coordinate": -1,
                                                        "Y-coordinate": -1,
                                                        "level": 1,
                                                        "last distance to goal": None,
                                                        "Strands": {"Red": 3.5, "Orange": 3,
                                                                    "Yellow": 3.5,
                                                                    "Green": 3,
                                                                    "Blue": 3.5, "Violet": 3.5}})
        expected = []
        self.assertEqual(expected, actual)


    def test_find_colours_with_0_strands_one_strand_colour_0(self):
        actual = character.find_colours_with_0_strands({"X-coordinate": -1,
                                                        "Y-coordinate": -1,
                                                        "level": 1,
                                                        "last distance to goal": None,
                                                        "Strands": {"Red": 0, "Orange": 3,
                                                                    "Yellow": 3,
                                                                    "Green": 3,
                                                                    "Blue": 3, "Violet": 3}})
        expected = ["Red"]
        self.assertEqual(expected, actual)


    def test_find_colours_with_0_strands_two_strand_colours_0(self):
        actual = character.find_colours_with_0_strands({"X-coordinate": -1,
                                                        "Y-coordinate": -1,
                                                        "level": 1,
                                                        "last distance to goal": None,
                                                        "Strands": {"Red": 0, "Orange": 3,
                                                                    "Yellow": 3,
                                                                    "Green": 3,
                                                                    "Blue": 3, "Violet": 0}})
        expected = ["Red", "Violet"]
        self.assertEqual(expected, actual)


    def test_find_colours_with_0_strands_most_strand_colours_0(self):
        actual = character.find_colours_with_0_strands({"X-coordinate": -1,
                                                        "Y-coordinate": -1,
                                                        "level": 1,
                                                        "last distance to goal": None,
                                                        "Strands": {"Red": 0, "Orange": 0,
                                                                    "Yellow": 0,
                                                                    "Green": 3,
                                                                    "Blue": 3, "Violet": 0}})
        expected = ["Red", "Orange", "Yellow", "Violet"]
        self.assertEqual(expected, actual)


    def test_find_colours_with_0_strands_one_strand_left(self):
        actual = character.find_colours_with_0_strands({"X-coordinate": -1,
                                                        "Y-coordinate": -1,
                                                        "level": 1,
                                                        "last distance to goal": None,
                                                        "Strands": {"Red": 0, "Orange": 0,
                                                                    "Yellow": 0,
                                                                    "Green": 0,
                                                                    "Blue": 1, "Violet": 0}})
        expected = ["Red", "Orange", "Yellow", "Green", "Violet"]
        self.assertEqual(expected, actual)


    def test_find_colours_with_0_strands_no_strands_left(self):
        actual = character.find_colours_with_0_strands({"X-coordinate": -1,
                                                        "Y-coordinate": -1,
                                                        "level": 1,
                                                        "last distance to goal": None,
                                                        "Strands": {"Red": 0, "Orange": 0,
                                                                    "Yellow": 0,
                                                                    "Green": 0,
                                                                    "Blue": 0, "Violet": 0}})
        expected = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
        self.assertEqual(expected, actual)


    def test_find_colours_with_0_strands_all_strands_one(self):
        actual = character.find_colours_with_0_strands({"X-coordinate": -1,
                                                        "Y-coordinate": -1,
                                                        "level": 1,
                                                        "last distance to goal": None,
                                                        "Strands": {"Red": 1, "Orange": 1,
                                                                    "Yellow": 1,
                                                                    "Green": 1,
                                                                    "Blue": 1, "Violet": 1}})
        expected = []
        self.assertEqual(expected, actual)


    def test_find_colours_with_0_strands_negative_strands(self):
        actual = character.find_colours_with_0_strands({"X-coordinate": -1,
                                                        "Y-coordinate": -1,
                                                        "level": 1,
                                                        "last distance to goal": None,
                                                        "Strands": {"Red": -1, "Orange": -2,
                                                                    "Yellow": -3,
                                                                    "Green": -2, "Blue": -1,
                                                                    "Violet": -1}})
        expected = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
        self.assertEqual(expected, actual)


    def test_find_colours_with_0_strands_raises_type_error_if_character_not_dict(self):
        with self.assertRaises(TypeError):
            character.find_colours_with_0_strands("X-coordinate")


    def test_find_colours_with_0_strands_raises_type_error_if_character_strands_not_dict(self):
        with self.assertRaises(TypeError):
            character.find_colours_with_0_strands({"X-coordinate": -1,
                                                   "Y-coordinate": -1,
                                                   "level": 1,
                                                   "last distance to goal": None,
                                                   "Strands": "thing"})


    def test_find_colours_with_0_strands_raises_type_error_if_character_strands_all_values_not_numbers(
            self):
        with self.assertRaises(TypeError):
            character.find_colours_with_0_strands({"X-coordinate": -1,
                                                   "Y-coordinate": -1,
                                                   "level": 1,
                                                   "last distance to goal": None,
                                                   "Strands": {"Red": "-1", "Orange": "-2",
                                                               "Yellow": "-3",
                                                               "Green": "-2", "Blue": "-1",
                                                               "Violet": "-1"}})


    def test_find_colours_with_0_strands_raises_type_error_if_character_strands_any_value_not_number(
            self):
        with self.assertRaises(TypeError):
            character.find_colours_with_0_strands({"X-coordinate": -1,
                                                   "Y-coordinate": -1,
                                                   "level": 1,
                                                   "last distance to goal": None,
                                                   "Strands": {"Red": -1, "Orange": -2,
                                                               "Yellow": -3,
                                                               "Green": -2, "Blue": -1,
                                                               "Violet": "-1"}})


    def test_find_colours_with_0_strands_raises_key_error_if_character_has_no_strands_key(self):
        with self.assertRaises(KeyError):
            character.find_colours_with_0_strands({"X-coordinate": -1,
                                                   "Y-coordinate": -1,
                                                   "level": 1,
                                                   "last distance to goal": None})
