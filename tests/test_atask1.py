import unittest

from atasks.atask1.atask1 import find_longest


class TestATask1(unittest.TestCase):
    def test_atask1_1(self):
        result = find_longest(1, [1, 2, 3, 5, 6, 10, 52])
        self.assertEqual([1, 3, 1, 3], result)

    def test_atask1_2(self):
        result = find_longest(2, [1, 3, 4,  5, 6, 10, 52])
        self.assertEqual([2, 4, 3, 6], result)

    def test_atask1_3(self):
        result = find_longest(3, [1, 10, 11, 13, 14, 49, 50,51, 52])
        self.assertEqual([3, 4, 49, 52], result)

    def test_atask1_4(self):
        result = find_longest(4, [1,4,5,50])
        self.assertEqual([4, 2, 4, 5], result)


if __name__ == '__main__':
    unittest.main()
