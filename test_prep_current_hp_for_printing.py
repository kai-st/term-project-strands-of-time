from unittest import TestCase


import game


class TestPrepCurrentHpForPrinting(TestCase):

    def test_prep_current_hp_for_printing_initial_hp(self):
        actual = game.prep_current_hp_for_printing({"X-coordinate": 0,
                                                           "Y-coordinate": 0,
                                                           "Current HP": 5})
        expected = 'Current HP: 5'
        self.assertEqual(expected, actual)

    def test_prep_current_hp_for_printing_mid_hp(self):
        actual = game.prep_current_hp_for_printing({"X-coordinate": 0,
                                                           "Y-coordinate": 0,
                                                           "Current HP": 3})
        expected = 'Current HP: 3'
        self.assertEqual(expected, actual)

    def test_prep_current_hp_for_printing_low_hp(self):
        actual = game.prep_current_hp_for_printing({"X-coordinate": 0,
                                                           "Y-coordinate": 0,
                                                           "Current HP": 1})
        expected = 'Current HP: 1'
        self.assertEqual(expected, actual)

    def test_prep_current_hp_for_printing_0_hp(self):
        actual = game.prep_current_hp_for_printing({"X-coordinate": 0,
                                                           "Y-coordinate": 0,
                                                           "Current HP": 0})
        expected = 'Current HP: 0'
        self.assertEqual(expected, actual)
