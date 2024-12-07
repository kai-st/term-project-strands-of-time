from unittest import TestCase
from unittest.mock import patch

import combat


class TestPercentageChanceResult(TestCase):

    @patch('random.randrange', return_value=99)
    def test_percentage_chance_100_percent_chance(self, _):
        actual = combat.percentage_chance_result(100)
        expected = True
        self.assertEqual(expected, actual)

    @patch('random.randrange', return_value=0)
    def test_percentage_chance_result_0_percent_chance(self, _):
        actual = combat.percentage_chance_result(0)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randrange', return_value=51)
    def test_percentage_chance_result_50_percent_chance_failure(self, _):
        actual = combat.percentage_chance_result(50)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randrange', return_value=50)
    def test_percentage_chance_result_50_percent_chance_fails_at_boundary_50(self, _):
        actual = combat.percentage_chance_result(50)
        expected = False
        self.assertEqual(expected, actual)

    @patch('random.randrange', return_value=49)
    def test_percentage_chance_result_50_percent_chance_success(self, _):
        actual = combat.percentage_chance_result(50)
        expected = True
        self.assertEqual(expected, actual)
