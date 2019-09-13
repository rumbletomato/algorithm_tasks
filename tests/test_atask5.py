import unittest

from atasks.atask5.atask5 import search_consecutive_set_of_numbers


class TestATask5(unittest.TestCase):
    def test_atask5_1(self):
        result = search_consecutive_set_of_numbers([1, 6, 43, 65, 3, 5], 7)
        self.assertEqual([0, 1], result)

    def test_atask5_2(self):
        result = search_consecutive_set_of_numbers([2, 6, 43, 65, 3, 5], 7)
        self.assertEqual('Sum was not found', result)

    def test_atask5_3(self):
        result = search_consecutive_set_of_numbers([1, 2, 3], 7)
        self.assertEqual('Sum was not found', result)

    def test_atask5_4(self):
        result = search_consecutive_set_of_numbers([5, 5, 5, 5, 5, 5, 5, 5, 5], 45)
        self.assertEqual([0, 8], result)

    def test_atask5_5(self):
        result = search_consecutive_set_of_numbers([8, 12, 9, 32, 3, 2, 1, 89, 21], 92)
        self.assertEqual([5, 7], result)
