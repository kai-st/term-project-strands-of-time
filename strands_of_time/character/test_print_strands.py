import io
from unittest import TestCase
from unittest.mock import patch


from strands_of_time.character import character


class TestPrintStrands(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_strands_level_1_initial_strands(self, mock_stdout):
        character.print_strands({"X-coordinate": 1,
                                "Y-coordinate": 1,
                                 "level": 1,
                                 "last distance to goal": None,
                                 "Strands": {"Red": 3, "Orange": 3, "Yellow": 3, "Green": 3,
                                             "Blue": 3, "Violet": 3}})
        expected = ("Strands: 1. \033[38;5;160mRed: 3\033[0m, 2. \033[38;5;208mOrange: 3\033[0m, "
                    "3. \033[38;5;220mYellow: 3\033[0m, 4. \033[38;5;41mGreen: 3\033[0m, "
                    "5. \033[38;5;33mBlue: 3\033[0m, 6. \033[38;5;135mViolet: 3\033[0m ")
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_strands_level_2_initial_strands(self, mock_stdout):
        character.print_strands({"X-coordinate": 1,
                                "Y-coordinate": 1,
                                 "level": 2,
                                 "last distance to goal": 4.7,
                                 "Strands": {"Red": 6, "Orange": 6, "Yellow": 6, "Green": 6,
                                             "Blue": 6, "Violet": 6}})
        expected = ("Strands: 1. \033[38;5;160mRed: 6\033[0m, 2. \033[38;5;208mOrange: 6\033[0m, "
                    "3. \033[38;5;220mYellow: 6\033[0m, 4. \033[38;5;41mGreen: 6\033[0m, "
                    "5. \033[38;5;33mBlue: 6\033[0m, 6. \033[38;5;135mViolet: 6\033[0m ")
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_strands_level_3_initial_strands(self, mock_stdout):
        character.print_strands({"X-coordinate": 1,
                                "Y-coordinate": 1,
                                 "level": 2,
                                 "last distance to goal": 4.7,
                                 "Strands": {"Red": 9, "Orange": 9, "Yellow": 9, "Green": 9,
                                             "Blue": 9, "Violet": 9}})
        expected = ("Strands: 1. \033[38;5;160mRed: 9\033[0m, 2. \033[38;5;208mOrange: 9\033[0m, "
                    "3. \033[38;5;220mYellow: 9\033[0m, 4. \033[38;5;41mGreen: 9\033[0m, "
                    "5. \033[38;5;33mBlue: 9\033[0m, 6. \033[38;5;135mViolet: 9\033[0m ")
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_strands_mixed_strand_amounts(self, mock_stdout):
        character.print_strands({"X-coordinate": 1,
                                "Y-coordinate": 1,
                                 "level": 2,
                                 "last distance to goal": 4.7,
                                 "Strands": {"Red": 9, "Orange": 2, "Yellow": 4, "Green": 0,
                                             "Blue": 6, "Violet": 1}})
        expected = ("Strands: 1. \033[38;5;160mRed: 9\033[0m, 2. \033[38;5;208mOrange: 2\033[0m, "
                    "3. \033[38;5;220mYellow: 4\033[0m, 4. \033[38;5;41mGreen: 0\033[0m, "
                    "5. \033[38;5;33mBlue: 6\033[0m, 6. \033[38;5;135mViolet: 1\033[0m ")
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_strands_all_strand_amounts_0(self, mock_stdout):
        character.print_strands({"X-coordinate": 1,
                                "Y-coordinate": 1,
                                 "level": 2,
                                 "last distance to goal": 4.7,
                                 "Strands": {"Red": 0, "Orange": 0, "Yellow": 0, "Green": 0,
                                             "Blue": 0, "Violet": 0}})
        expected = ("Strands: 1. \033[38;5;160mRed: 0\033[0m, 2. \033[38;5;208mOrange: 0\033[0m, "
                    "3. \033[38;5;220mYellow: 0\033[0m, 4. \033[38;5;41mGreen: 0\033[0m, "
                    "5. \033[38;5;33mBlue: 0\033[0m, 6. \033[38;5;135mViolet: 0\033[0m ")
        self.assertEqual(expected, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_strands_raises_type_error_if_character_not_dict(self, _):
        with self.assertRaises(TypeError):
            character.print_strands("X-coordinate")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_strands_raises_type_error_if_character_strands_not_dict(self, _):
        with self.assertRaises(TypeError):
            character.print_strands({"X-coordinate": 1,
                                     "Y-coordinate": 1,
                                     "level": 1,
                                     "last distance to goal": None,
                                     "Strands": "thing"})

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_strands_raises_key_error_if_character_has_no_strands_key(self, _):
        with self.assertRaises(KeyError):
            character.print_strands({"X-coordinate": 1,
                                    "Y-coordinate": 1,
                                     "level": 1,
                                     "last distance to goal": None})
