from unittest import TestCase

import strands_of_time.character.character
from strands_of_time import game


class TestDamageCharacter(TestCase):

    def test_damage_character_full_health(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        strands_of_time.character.character.damage_character(test_character)
        actual = test_character["Current HP"]
        expected = 4
        self.assertEqual(expected, actual)

    def test_damage_character_dying(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 1}
        strands_of_time.character.character.damage_character(test_character)
        actual = test_character["Current HP"]
        expected = 0
        self.assertEqual(expected, actual)

    def test_damage_character_mid_hp(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 3}
        strands_of_time.character.character.damage_character(test_character)
        actual = test_character["Current HP"]
        expected = 2
        self.assertEqual(expected, actual)

    def test_damage_character_does_not_change_x(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        strands_of_time.character.character.damage_character(test_character)
        actual = test_character["X-coordinate"]
        expected = 3
        self.assertEqual(expected, actual)

    def test_damage_character_does_not_change_y(self):
        test_character = {"X-coordinate": 3, "Y-coordinate": 3, "Current HP": 5}
        strands_of_time.character.character.damage_character(test_character)
        actual = test_character["Y-coordinate"]
        expected = 3
        self.assertEqual(expected, actual)
