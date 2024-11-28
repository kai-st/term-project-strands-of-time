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

