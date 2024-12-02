from unittest import TestCase


import game


class TestColourize(TestCase):

    def test_colourize_makes_message_Red(self):
        actual = game.colourize("My message", "Red")
        expected = "\033[38;5;160mMy message\033[0m"
        self.assertEqual(expected, actual)

    def test_colourize_makes_message_Orange(self):
        actual = game.colourize("My message", "Orange")
        expected = "\033[38;5;208mMy message\033[0m"
        self.assertEqual(expected, actual)

    def test_colourize_makes_message_Yellow(self):
        actual = game.colourize("My message", "Yellow")
        expected = "\033[38;5;220mMy message\033[0m"
        self.assertEqual(expected, actual)

    def test_colourize_makes_message_Green(self):
        actual = game.colourize("My message", "Green")
        expected = "\033[38;5;41mMy message\033[0m"
        self.assertEqual(expected, actual)

    def test_colourize_makes_message_Blue(self):
        actual = game.colourize("My message", "Blue")
        expected = "\033[38;5;33mMy message\033[0m"
        self.assertEqual(expected, actual)

    def test_colourize_makes_message_Violet(self):
        actual = game.colourize("My message", "Violet")
        expected = "\033[38;5;135mMy message\033[0m"
        self.assertEqual(expected, actual)

    def test_colourize_makes_message_Pink(self):
        actual = game.colourize("My message", "Pink")
        expected = "\033[38;5;207mMy message\033[0m"
        self.assertEqual(expected, actual)

    def test_colourize_raises_type_error_if_message_not_string(self):
        with self.assertRaises(TypeError):
            game.colourize(123, "Red")

    def test_colourize_raises_type_error_if_colour_not_string(self):
        with self.assertRaises(TypeError):
            game.colourize("123", 1)

    def test_colourize_raises_value_error_if_colour_not_available(self):
        with self.assertRaises(ValueError):
            game.colourize("123", "Brown")
