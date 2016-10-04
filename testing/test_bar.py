import unittest
import os
from webExtract.bar_generator import BarTool

bt = BarTool()
t_list = bt.data_collector(location=os.path.pardir)


class TestBarMethods(unittest.TestCase):

    def test_data_collector(self):
        t = ([5, 22, 19, 8, 6, 1, 25, 20], [2, 10, 8, 3, 5, 1, 0, 8])
        self.assertEqual(t_list, t)

    def test_data_1(self):
        ls_1 = [5, 22, 19, 8, 6, 1, 25, 20]
        self.assertEqual(t_list[0], ls_1)

    def test_data_2(self):
        ls_2 = [2, 10, 8, 3, 5, 1, 0, 8]
        self.assertEqual(t_list[1], ls_2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
