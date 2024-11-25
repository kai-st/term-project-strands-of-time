from unittest import TestCase
from unittest.mock import patch

from strands_of_time import game


class TestCheckForFoes(TestCase):

    @patch('random.randint', return_value=1)
    def test_check_for_foes_on_a_1(self, _):
        actual = game.check_for_foes()
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_check_for_foes_on_a_2(self, _):
        actual = game.check_for_foes()
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_check_for_foes_on_a_3(self, _):
        actual = game.check_for_foes()
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=4)
    def test_check_for_foes_on_a_4(self, _):
        actual = game.check_for_foes()
        expected = True
        self.assertEqual(expected, actual)
