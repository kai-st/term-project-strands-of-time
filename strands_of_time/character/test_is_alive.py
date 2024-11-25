from unittest import TestCase

from strands_of_time import game


class TestIsAlive(TestCase):

    def test_is_alive_returns_Boolean(self):
        actual = type(game.has_strands({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}))
        expected = type(True)
        self.assertEqual(expected, actual)

    def test_is_alive_initial_hp(self):
        actual = game.has_strands({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5})
        expected = True
        self.assertEqual(expected, actual)

    def test_is_alive_mid_hp(self):
        actual = game.has_strands({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 3})
        expected = True
        self.assertEqual(expected, actual)

    def test_is_alive_low_hp(self):
        actual = game.has_strands({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 1})
        expected = True
        self.assertEqual(expected, actual)

    def test_is_alive_0_hp(self):
        actual = game.has_strands({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 0})
        expected = False
        self.assertEqual(expected, actual)

    def test_is_alive_negative_hp(self):
        actual = game.has_strands({"X-coordinate": 0, "Y-coordinate": 0, "Current HP": -1})
        expected = False
        self.assertEqual(expected, actual)
