import os
import unittest
from webExtract.game_displayer import HTML2Game


class TestH2GMethods(unittest.TestCase):

    def test_get_urls(self):
        entireUrl = 'https://www.mightyape.co.nz/games/ps4/adventure-rpg/All?page='
        h2g = HTML2Game('https://www.mightyape.co.nz')
        expected_quantity = 113
        real_result = len(h2g.get_urls(entireUrl))
        self.assertEqual(real_result, expected_quantity)

    def test_unserializing_game(self):
        # path = os.path.dirname(os.path.abspath("__file__"))
        path = os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))
        entireUrl = 'https://www.mightyape.co.nz/games/ps4/adventure-rpg/All?page='
        h2g = HTML2Game('https://www.mightyape.co.nz')
        games = h2g.unserializing_game(path)
        expected_quantity = 113
        real_result = len(games)
        self.assertEqual(real_result, expected_quantity)

if __name__ == '__main__':
    unittest.main()