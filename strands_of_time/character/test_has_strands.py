from unittest import TestCase

import character


class TestHasStrands(TestCase):

    def test_has_strands_returns_Boolean(self):
        actual = type(
            character.has_strands({"X-coordinate": -1,
                                  "Y-coordinate": -1,
                                   "level": 1,
                                   "last distance to goal": None,
                                   "Strands": {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3,
                                               "Blue": 3, "Violet": 3}}))
        expected = type(True)
        self.assertEqual(expected, actual)

    def test_has_strands_initial_strands(self):
        actual = character.has_strands({"X-coordinate": -1,
                                        "Y-coordinate": -1,
                                        "level": 1,
                                        "last distance to goal": None,
                                        "Strands": {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3,
                                                    "Blue": 3, "Violet": 3}})
        expected = True
        self.assertEqual(expected, actual)

    def test_has_strands_strands_can_be_floats(self):
        actual = character.has_strands({"X-coordinate": -1,
                                        "Y-coordinate": -1,
                                        "level": 1,
                                        "last distance to goal": None,
                                        "Strands": {"Red": 3.5, "Orange": 3.5, "Yellow": 3.5,
                                                    "Green": 3.5,
                                                    "Blue": 3.5, "Violet": 3.5}})
        expected = True
        self.assertEqual(expected, actual)

    def test_has_strands_strands_can_mix_ints_and_floats(self):
        actual = character.has_strands({"X-coordinate": -1,
                                        "Y-coordinate": -1,
                                        "level": 1,
                                        "last distance to goal": None,
                                        "Strands": {"Red": 3.5, "Orange": 3, "Yellow": 3.5,
                                                    "Green": 3,
                                                    "Blue": 3.5, "Violet": 3.5}})
        expected = True
        self.assertEqual(expected, actual)

    def test_has_strands_one_strand_colour_0(self):
        actual = character.has_strands({"X-coordinate": -1,
                                        "Y-coordinate": -1,
                                        "level": 1,
                                        "last distance to goal": None,
                                        "Strands": {"Red": 0, "Orange": 3, "Yellow": 3, "Green": 3,
                                                    "Blue": 3, "Violet": 3}})
        expected = True
        self.assertEqual(expected, actual)

    def test_has_strands_two_strand_colours_0(self):
        actual = character.has_strands({"X-coordinate": -1,
                                        "Y-coordinate": -1,
                                        "level": 1,
                                        "last distance to goal": None,
                                        "Strands": {"Red": 0, "Orange": 3, "Yellow": 3, "Green": 3,
                                                    "Blue": 3, "Violet": 0}})
        expected = True
        self.assertEqual(expected, actual)

    def test_has_strands_most_strand_colours_0(self):
        actual = character.has_strands({"X-coordinate": -1,
                                        "Y-coordinate": -1,
                                        "level": 1,
                                        "last distance to goal": None,
                                        "Strands": {"Red": 0, "Orange": 0, "Yellow": 0, "Green": 3,
                                                    "Blue": 3, "Violet": 0}})
        expected = True
        self.assertEqual(expected, actual)

    def test_has_strands_one_strand_left(self):
        actual = character.has_strands({"X-coordinate": -1,
                                        "Y-coordinate": -1,
                                        "level": 1,
                                        "last distance to goal": None,
                                        "Strands": {"Red": 0, "Orange": 0, "Yellow": 0, "Green": 0,
                                                    "Blue": 1, "Violet": 0}})

    def test_has_strands_no_strands_left(self):
        actual = character.has_strands({"X-coordinate": -1,
                                        "Y-coordinate": -1,
                                        "level": 1,
                                        "last distance to goal": None,
                                        "Strands": {"Red": 0, "Orange": 0, "Yellow": 0, "Green": 0,
                                                    "Blue": 0, "Violet": 0}})
        expected = False
        self.assertEqual(expected, actual)

    def test_has_strands_negative_strands(self):
        actual = character.has_strands({"X-coordinate": -1,
                                        "Y-coordinate": -1,
                                        "level": 1,
                                        "last distance to goal": None,
                                        "Strands": {"Red": -1, "Orange": -2, "Yellow": -3,
                                                    "Green": -2, "Blue": -1, "Violet": -1}})
        expected = False
        self.assertEqual(expected, actual)

    def test_has_strands_raises_type_error_if_character_not_dict(self):
        with self.assertRaises(TypeError):
            character.has_strands("X-coordinate")

    def test_has_strands_raises_type_error_if_character_strands_not_dict(self):
        with self.assertRaises(TypeError):
            character.has_strands({"X-coordinate": -1,
                                  "Y-coordinate": -1,
                                   "level": 1,
                                   "last distance to goal": None,
                                   "Strands": "thing"})

    def test_has_strands_raises_value_error_if_character_strands_all_values_not_numbers(self):
        with self.assertRaises(ValueError):
            character.has_strands({"X-coordinate": -1,
                                  "Y-coordinate": -1,
                                   "level": 1,
                                   "last distance to goal": None,
                                   "Strands": {"Red": "-1", "Orange": "-2", "Yellow": "-3",
                                               "Green": "-2", "Blue": "-1", "Violet": "-1"}})

    def test_has_strands_raises_value_error_if_character_strands_any_value_not_number(self):
        with self.assertRaises(ValueError):
            character.has_strands({"X-coordinate": -1,
                                  "Y-coordinate": -1,
                                   "level": 1,
                                   "last distance to goal": None,
                                   "Strands": {"Red": -1, "Orange": -2, "Yellow": -3,
                                               "Green": -2, "Blue": -1, "Violet": "-1"}})

    def test_has_strands_raises_key_error_if_character_has_no_strands_key(self):
        with self.assertRaises(KeyError):
            character.has_strands({"X-coordinate": -1,
                                  "Y-coordinate": -1,
                                   "level": 1,
                                   "last distance to goal": None})


