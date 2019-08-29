import unittest

from atasks.atask3.atask3 import clever_sort


class TestATask3(unittest.TestCase):
    def test_atask3_1(self):
        result = clever_sort([1, 2, 3, 4, 5, 6, 7], [5, 7, 3])
        self.assertEqual([3, 5, 7], result)

    def test_atask3_2(self):
        result = clever_sort(['one', 'two', 'three', 'four', 'five'], ['three', 'one', 'four'])
        self.assertEqual(['one', 'three', 'four'], result)
