from unittest import TestCase
from unittest.mock import patch


from strands_of_time.character import character


class TestRemoveRandomStrand(TestCase):

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_from_level_1_initial_strands(self, _):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 1,
                          "last distance to goal": None,
                          "Strands": {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3,
                                      "Blue": 3, "Violet": 3}}
        character.remove_random_strand(test_character)
        actual = test_character["Strands"]
        expected = {"Red": 2, "Orange": 3, "Yellow": 3, "Green": 3, "Blue": 3, "Violet": 3}
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_from_level_2_initial_strands(self, _):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 2,
                          "last distance to goal": None,
                          "Strands": {"Red": 6, "Orange": 6, "Yellow": 6, "Green": 6,
                                      "Blue": 6, "Violet": 6}}
        character.remove_random_strand(test_character)
        actual = test_character["Strands"]
        expected = {"Red": 5, "Orange": 6, "Yellow": 6, "Green": 6, "Blue": 6, "Violet": 6}
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_from_level_3_initial_strands(self, _):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 3,
                          "last distance to goal": None,
                          "Strands": {"Red": 9, "Orange": 9, "Yellow": 9, "Green": 9,
                                      "Blue": 9, "Violet": 9}}
        character.remove_random_strand(test_character)
        actual = test_character["Strands"]
        expected = {"Red": 8, "Orange": 9, "Yellow": 9, "Green": 9, "Blue": 9, "Violet": 9}
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_red_strand(self, _):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 3,
                          "last distance to goal": None,
                          "Strands": {"Red": 9, "Orange": 9, "Yellow": 9, "Green": 9,
                                      "Blue": 9, "Violet": 8}}
        character.remove_random_strand(test_character)
        actual = test_character["Strands"]
        expected = {"Red": 8, "Orange": 9, "Yellow": 9, "Green": 9, "Blue": 9, "Violet": 8}
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value="Orange")
    def test_remove_random_strand_orange_strand(self, _):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 3,
                          "last distance to goal": None,
                          "Strands": {"Red": 9, "Orange": 9, "Yellow": 9, "Green": 9,
                                      "Blue": 9, "Violet": 8}}
        character.remove_random_strand(test_character)
        actual = test_character["Strands"]
        expected = {"Red": 9, "Orange": 8, "Yellow": 9, "Green": 9, "Blue": 9, "Violet": 8}
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value="Yellow")
    def test_remove_random_strand_yellow_strand(self, _):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 3,
                          "last distance to goal": None,
                          "Strands": {"Red": 9, "Orange": 9, "Yellow": 9, "Green": 9,
                                      "Blue": 9, "Violet": 8}}
        character.remove_random_strand(test_character)
        actual = test_character["Strands"]
        expected = {"Red": 9, "Orange": 9, "Yellow": 8, "Green": 9, "Blue": 9, "Violet": 8}
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value="Green")
    def test_remove_random_strand_green_strand(self, _):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 3,
                          "last distance to goal": None,
                          "Strands": {"Red": 9, "Orange": 9, "Yellow": 9, "Green": 9,
                                      "Blue": 9, "Violet": 8}}
        character.remove_random_strand(test_character)
        actual = test_character["Strands"]
        expected = {"Red": 9, "Orange": 9, "Yellow": 9, "Green": 8, "Blue": 9, "Violet": 8}
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value="Blue")
    def test_remove_random_strand_blue_strand(self, _):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 3,
                          "last distance to goal": None,
                          "Strands": {"Red": 9, "Orange": 9, "Yellow": 9, "Green": 9,
                                      "Blue": 9, "Violet": 8}}
        character.remove_random_strand(test_character)
        actual = test_character["Strands"]
        expected = {"Red": 9, "Orange": 9, "Yellow": 9, "Green": 9, "Blue": 8, "Violet": 8}
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value="Violet")
    def test_remove_random_strand_violet_strand(self, _):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 3,
                          "last distance to goal": None,
                          "Strands": {"Red": 9, "Orange": 9, "Yellow": 9, "Green": 9,
                                      "Blue": 9, "Violet": 9}}
        character.remove_random_strand(test_character)
        actual = test_character["Strands"]
        expected = {"Red": 9, "Orange": 9, "Yellow": 9, "Green": 9, "Blue": 9, "Violet": 8}
        self.assertEqual(expected, actual)

    def test_remove_random_removes_last_strand(self):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 3,
                          "last distance to goal": None,
                          "Strands": {"Red": 1, "Orange": 0, "Yellow": 0, "Green": 0,
                                      "Blue": 0, "Violet": 0}}
        character.remove_random_strand(test_character)
        actual = test_character["Strands"]
        expected = {"Red": 0, "Orange": 0, "Yellow": 0, "Green": 0, "Blue": 0, "Violet": 0}
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_mixed_strand_amounts_without_0(self, _):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 3,
                          "last distance to goal": None,
                          "Strands": {"Red": 5, "Orange": 1, "Yellow": 3, "Green": 8,
                                      "Blue": 9, "Violet": 2}}
        character.remove_random_strand(test_character)
        actual = test_character["Strands"]
        expected = {"Red": 4, "Orange": 1, "Yellow": 3, "Green": 8, "Blue": 9, "Violet": 2}
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_mixed_strand_amounts_with_0(self, _):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 3,
                          "last distance to goal": None,
                          "Strands": {"Red": 5, "Orange": 0, "Yellow": 3, "Green": 8,
                                      "Blue": 0, "Violet": 2}}
        character.remove_random_strand(test_character)
        actual = test_character["Strands"]
        expected = {"Red": 4, "Orange": 0, "Yellow": 3, "Green": 8, "Blue": 0, "Violet": 2}
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_mixed_strand_amounts_with_negative(self, _):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 3,
                          "last distance to goal": None,
                          "Strands": {"Red": 5, "Orange": 0, "Yellow": -3, "Green": 8,
                                      "Blue": 0, "Violet": 2}}
        character.remove_random_strand(test_character)
        actual = test_character["Strands"]
        expected = {"Red": 4, "Orange": 0, "Yellow": -3, "Green": 8, "Blue": 0, "Violet": 2}
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_does_not_change_x(self, _):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 3,
                          "last distance to goal": None,
                          "Strands": {"Red": 5, "Orange": 1, "Yellow": 3, "Green": 8,
                                      "Blue": 9, "Violet": 2}}
        character.remove_random_strand(test_character)
        actual = test_character["X-coordinate"]
        expected = 2
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_does_not_change_y(self, _):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 3,
                          "last distance to goal": None,
                          "Strands": {"Red": 5, "Orange": 1, "Yellow": 3, "Green": 8,
                                      "Blue": 9, "Violet": 2}}
        character.remove_random_strand(test_character)
        actual = test_character["Y-coordinate"]
        expected = 3
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_does_not_change_level(self, _):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 3,
                          "last distance to goal": None,
                          "Strands": {"Red": 5, "Orange": 1, "Yellow": 3, "Green": 8,
                                      "Blue": 9, "Violet": 2}}
        character.remove_random_strand(test_character)
        actual = test_character["level"]
        expected = 3
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_does_not_change_last_distance_to_goal(self, _):
        test_character = {"X-coordinate": 2,
                          "Y-coordinate": 3,
                          "level": 3,
                          "last distance to goal": 4.76,
                          "Strands": {"Red": 5, "Orange": 1, "Yellow": 3, "Green": 8,
                                      "Blue": 9, "Violet": 2}}
        character.remove_random_strand(test_character)
        actual = test_character["last distance to goal"]
        expected = 4.76
        self.assertEqual(expected, actual)

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_raises_type_error_if_character_not_dict(self, _):
        with self.assertRaises(TypeError):
            character.remove_random_strand("X-coordinate")

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_raises_type_error_if_character_strands_not_dict(self, _):
        with self.assertRaises(TypeError):
            character.remove_random_strand({"X-coordinate": 1,
                                           "Y-coordinate": 1,
                                            "level": 1,
                                            "last distance to goal": None,
                                            "Strands": "thing"})

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_raises_type_error_if_character_strands_all_values_not_numbers(
            self, _):
        with self.assertRaises(TypeError):
            character.remove_random_strand({"X-coordinate": 1,
                                           "Y-coordinate": 1,
                                            "level": 1,
                                            "last distance to goal": None,
                                            "Strands": {"Red": "1", "Orange": "2", "Yellow": "3",
                                                        "Green": "2", "Blue": "1", "Violet": "1"}})

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_raises_type_error_if_character_strands_any_value_not_number(
            self, _):
        with self.assertRaises(TypeError):
            character.remove_random_strand({"X-coordinate": 1,
                                           "Y-coordinate": 1,
                                            "level": 1,
                                            "last distance to goal": None,
                                            "Strands": {"Red": 1, "Orange": 2, "Yellow": 3,
                                                        "Green": 2, "Blue": 1, "Violet": "1"}})

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_raises_value_error_if_character_strands_all_0(self, _):
        with self.assertRaises(ValueError):
            character.remove_random_strand({"X-coordinate": 1,
                                           "Y-coordinate": 1,
                                            "level": 1,
                                            "last distance to goal": None,
                                            "Strands": {"Red": 0, "Orange": 0, "Yellow": 0,
                                                        "Green": 0, "Blue": 0, "Violet": 0}})

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_raises_value_error_if_character_strands_all_negative(self, _):
        with self.assertRaises(ValueError):
            character.remove_random_strand({"X-coordinate": 1,
                                           "Y-coordinate": 1,
                                            "level": 1,
                                            "last distance to goal": None,
                                            "Strands": {"Red": -1, "Orange": -1, "Yellow": -1,
                                                        "Green": -1, "Blue": -1, "Violet": -1}})

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_raises_value_error_if_character_strands_0_or_negative(self, _):
        with self.assertRaises(ValueError):
            character.remove_random_strand({"X-coordinate": 1,
                                           "Y-coordinate": 1,
                                            "level": 1,
                                            "last distance to goal": None,
                                            "Strands": {"Red": -1, "Orange": 0, "Yellow": -1,
                                                        "Green": -1, "Blue": 0, "Violet": 0}})

    @patch('random.choice', return_value="Red")
    def test_remove_random_strand_raises_key_error_if_character_has_no_strands_key(self, _):
        with self.assertRaises(KeyError):
            character.remove_random_strand({"X-coordinate": 1,
                                           "Y-coordinate": 1,
                                            "level": 1,
                                            "last distance to goal": None})
