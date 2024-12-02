from unittest import TestCase

import character


class TestGetCharacterLocationAsTuple(TestCase):

    def test_get_character_location_as_tuple_returns_tuple(self):
        test_character = {"X-coordinate": 1,
                          "Y-coordinate": 1,
                          "level": 1,
                          "last distance to goal": None,
                          "Strands": {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3,
                                      "Blue": 3, "Violet": 3}}
        actual = type(
            character.get_character_location_as_tuple(test_character))
        expected = type((1, 1))
        self.assertEqual(expected, actual)

    def test_get_character_location_as_tuple_X_at_index_0(self):
        test_character = {"X-coordinate": 1,
                          "Y-coordinate": 2,
                          "level": 1,
                          "last distance to goal": None,
                          "Strands": {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3,
                                      "Blue": 3, "Violet": 3}}
        location = character.get_character_location_as_tuple(test_character)
        actual = location[0]
        expected = test_character["X-coordinate"]
        self.assertEqual(expected, actual)

    def test_get_character_location_as_tuple_Y_at_index_1(self):
        test_character = {"X-coordinate": 1,
                          "Y-coordinate": 2,
                          "level": 1,
                          "last distance to goal": None,
                          "Strands": {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3,
                                      "Blue": 3, "Violet": 3}}
        location = character.get_character_location_as_tuple(test_character)
        actual = location[1]
        expected = test_character["Y-coordinate"]
        self.assertEqual(expected, actual)

    def test_get_character_location_as_tuple_initial_location(self):
        test_character = {"X-coordinate": -1,
                          "Y-coordinate": -1,
                          "level": 1,
                          "last distance to goal": None,
                          "Strands": {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3,
                                      "Blue": 3, "Violet": 3}}
        actual = character.get_character_location_as_tuple(test_character)
        expected = (-1, -1)
        self.assertEqual(expected, actual)

    def test_get_character_location_as_tuple_max_location(self):
        test_character = {"X-coordinate": 8,
                          "Y-coordinate": 2,
                          "level": 1,
                          "last distance to goal": None,
                          "Strands": {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3,
                                      "Blue": 3, "Violet": 3}}
        actual = character.get_character_location_as_tuple(test_character)
        expected = (8, 2)
        self.assertEqual(expected, actual)

    def test_get_character_location_as_tuple_location_X_2_Y_3(self):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 1,
                          "last distance to goal": None,
                          "Strands": {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3,
                                      "Blue": 3, "Violet": 3}}
        actual = character.get_character_location_as_tuple(test_character)
        expected = (2, 3)
        self.assertEqual(expected, actual)

    def test_get_character_location_as_tuple_raises_type_error_if_character_not_dict(self):
        with self.assertRaises(TypeError):
            character.get_character_location_as_tuple("X-coordinate")

    def test_get_character_location_as_tuple_raises_key_error_if_no_x_coordinate(self):
        with self.assertRaises(KeyError):
            test_character = {"Y-coordinate": 3,
                              "level": 1,
                              "last distance to goal": None,
                              "Strands": {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3,
                                          "Blue": 3, "Violet": 3}}
            character.get_character_location_as_tuple(test_character)

    def test_get_character_location_as_tuple_raises_key_error_if_no_y_coordinate(self):
        with self.assertRaises(KeyError):
            test_character = {"X-coordinate": 2,
                              "level": 1,
                              "last distance to goal": None,
                              "Strands": {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3,
                                          "Blue": 3, "Violet": 3}}
            character.get_character_location_as_tuple(test_character)
