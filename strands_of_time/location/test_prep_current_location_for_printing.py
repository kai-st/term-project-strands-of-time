from unittest import TestCase

import strands_of_time.location.board
from strands_of_time import game


class TestPrepCurrentLocationForPrinting(TestCase):

    def test_prep_current_location_for_printing_initial_location(self):
        test_character = {"X-coordinate": 0, "Y-coordinate": 0, "Current HP": 5}
        actual = strands_of_time.location.board.print_current_epoch(test_character)
        expected = 'Current location: Row 1, Column 1'
        self.assertEqual(expected, actual)

    def test_prep_current_location_for_printing_goal_location(self):
        test_character = {"X-coordinate": 4, "Y-coordinate": 4, "Current HP": 5}
        actual = strands_of_time.location.board.print_current_epoch(test_character)
        expected = 'Current location: Row 5, Column 5'
        self.assertEqual(expected, actual)

    def test_prep_current_location_for_printing_location_X_2_Y_3(self):
        test_character = {"X-coordinate": 2, "Y-coordinate": 3, "Current HP": 5}
        actual = strands_of_time.location.board.print_current_epoch(test_character)
        expected = 'Current location: Row 4, Column 3'
        self.assertEqual(expected, actual)
