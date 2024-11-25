from unittest import TestCase
from unittest.mock import patch


import game


class TestPickTypeOfFoe(TestCase):

    @patch('random.choice', return_value="drow")
    def test_pick_type_of_foe_drow(self, _):
        actual = game.pick_type_of_foe()
        expected = "drow"
        self.assertEqual(expected, actual)

    def test_pick_type_of_foe_in_list(self):
        enemies = ["giant spider", "drow", "drider", "duergar", "mind flayer",
                   "intellect devourer", "myconid", "gelationous cube", "beholder",
                   "swarm of cranium rats", "kuo-toa", "carrion crawler", "troll",
                   "swarm of bats"]
        actual = game.pick_type_of_foe()
        self.assertIn(actual, enemies)
