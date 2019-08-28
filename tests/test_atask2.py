import unittest

from atasks.atask2.atask2 import merge_intervals


class TestATask2(unittest.TestCase):
    def test_atask2_1(self):
        result = merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]])
        self.assertEqual([[1, 6], [8, 10], [15, 18]], result)

    def test_atask2_2(self):
        result = merge_intervals([[1, 3], [2, 6], [8, 10], [11, 15], [15, 18]])
        self.assertEqual([[1, 6], [8, 10], [11, 18]], result)
