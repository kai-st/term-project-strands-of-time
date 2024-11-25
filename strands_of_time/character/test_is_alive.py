from unittest import TestCase

import character


class TestHasStrands(TestCase):

    def test_has_strands_returns_Boolean(self):
        actual = type(
            character.has_strands({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}))
        expected = type(True)
        self.assertEqual(expected, actual)

    def test_has_strands_initial_hp(self):
        actual = character.has_strands({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5})
        expected = True
        self.assertEqual(expected, actual)

    def test_has_strands_mid_hp(self):
        actual = character.has_strands({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 3})
        expected = True
        self.assertEqual(expected, actual)

    def test_has_strands_low_hp(self):
        actual = character.has_strands({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 1})
        expected = True
        self.assertEqual(expected, actual)

    def test_has_strands_0_hp(self):
        actual = character.has_strands({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 0})
        expected = False
        self.assertEqual(expected, actual)

    def test_has_strands_negative_hp(self):
        actual = character.has_strands({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": -1})
        expected = False
        self.assertEqual(expected, actual)
