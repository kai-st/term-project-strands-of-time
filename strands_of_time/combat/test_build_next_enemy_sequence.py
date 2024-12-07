from unittest import TestCase


import combat


class TestBuildNextEnemySequence(TestCase):

    def test_build_next_enemy_sequence_empty_lists(self):
        actual = combat.build_next_enemy_sequence([], [])
        expected = []
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_1_item_thread_0(self):
        actual = combat.build_next_enemy_sequence([2], [0])
        expected = [2]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_1_item_thread_neg_1(self):
        actual = combat.build_next_enemy_sequence([2], [-1])
        expected = [2]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_1_item_thread_1(self):
        actual = combat.build_next_enemy_sequence([2], [1])
        expected = [2]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_multiple_items_single_thread_number(self):
        actual = combat.build_next_enemy_sequence([2, 4, 1, 0, 3], [1, 1, 1, 1, 1])
        expected = [2, 4, 1, 0, 3]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_2_items_threads_0_neg_1(self):
        actual = combat.build_next_enemy_sequence([1, 2], [0, -1])
        expected = [1, 2]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_2_items_threads_1_0(self):
        actual = combat.build_next_enemy_sequence([1, 2], [1, 0])
        expected = [1, 2]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_2_items_threads_neg_1_0(self):
        actual = combat.build_next_enemy_sequence([1, 2], [-1, 0])
        expected = [1, 2]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_2_items_threads_neg_1_1(self):
        actual = combat.build_next_enemy_sequence([1, 2], [-1, 1])
        expected = [1, 2]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_2_items_threads_1_neg_1(self):
        actual = combat.build_next_enemy_sequence([1, 2], [1, -1])
        expected = [2, 1]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_3_items_middle_thread_0_ends_different_swap(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3], [1, 0, -1])
        expected = [3, 2, 1]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_3_items_middle_thread_0_ends_1(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3], [1, 0, 1])
        expected = [1, 2, 3]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_3_items_middle_thread_0_ends_neg_1(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3], [-1, 0, -1])
        expected = [1, 2, 3]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_3_items_middle_thread_0_ends_different_no_swap(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3], [-1, 0, 1])
        expected = [1, 2, 3]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_3_items_first_thread_0_swap(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3], [0, 1, -1])
        expected = [1, 3, 2]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_3_items_first_thread_0_no_swap(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3], [0, -1, 1])
        expected = [1, 2, 3]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_3_items_last_thread_0_swap(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3], [1, -1, 0])
        expected = [2, 1, 3]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_3_items_last_thread_0_no_swap(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3], [-1, 1, 0])
        expected = [1, 2, 3]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_3_items_no_0_no_swap_two_1s(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3], [-1, 1, 1])
        expected = [1, 2, 3]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_3_items_no_0_no_swap_two_neg_1s(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3], [-1, -1, 1])
        expected = [1, 2, 3]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_3_items_no_0_swap_two_1s(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3], [1, 1, -1])
        expected = [3, 1, 2]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_3_items_no_0_swap_two_neg_1s(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3], [1, -1, -1])
        expected = [2, 3, 1]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_3_items_no_0_split_neg_1s(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3], [-1, 1, -1])
        expected = [1, 3, 2]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_3_items_no_0_split_1s(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3], [1, -1, 1])
        expected = [2, 1, 3]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_alternating_swaps(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3, 4], [1, -1, 1, -1])
        expected = [2, 1, 4, 3]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_middle_swap(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3, 4], [-1, 1, -1, 1])
        expected = [1, 3, 2, 4]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_3_neg_1s(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3, 4], [-1, 1, -1, -1])
        expected = [1, 3, 4, 2]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_3_1s(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3, 4], [1, 1, -1, 1])
        expected = [3, 1, 2, 4]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_swap_skipping_0(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3, 4], [1, 0, -1, -1])
        expected = [3, 2, 4, 1]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_swap_with_blocking_0(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3, 4], [1, -1, 0, -1])
        expected = [2, 1, 3, 4]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_swap_around_0(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3, 4, 5], [1, 1, 0, -1, -1])
        expected = [4, 5, 3, 1, 2]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_lopsided_swap_right(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3, 4, 5], [1, 1, 1, 1, -1])
        expected = [5, 1, 2, 3, 4]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_lopsided_swap_left(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3, 4, 5], [1, -1, -1, -1, -1])
        expected = [2, 3, 4, 5, 1]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_0_takes_precedence(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3, 4, 5], [1, 1, 0, 1, -1])
        expected = [5, 1, 3, 2, 4]
        self.assertEqual(expected, actual)

    def test_build_next_enemy_sequence_outside_neg_1s(self):
        actual = combat.build_next_enemy_sequence([1, 2, 3, 4, 5], [-1, 1, 1, 1, -1])
        expected = [1, 5, 2, 3, 4]
        self.assertEqual(expected, actual)
