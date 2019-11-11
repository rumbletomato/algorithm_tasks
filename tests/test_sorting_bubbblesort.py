import random
from unittest import TestCase

from atasks.sorting.bubblesort import dummy_bubblesort, classic_bubblesort, cocktail_bubblesort, comb_bubblesort


class TestSortingBubblesort(TestCase):
    DATASET_LENGTH = 1000
    MIN_VALUE = -99
    MAX_VALUE = 99

    def setUp(self) -> None:
        super().setUp()

        self.unsorted_dataset = [random.randrange(self.MIN_VALUE, self.MAX_VALUE) for _ in range(self.DATASET_LENGTH)]
        self.sorted_dataset = sorted(self.unsorted_dataset)

    def test_check_input(self) -> None:
        self.assertRaises(TypeError, dummy_bubblesort, None)

    def test_empty_array(self) -> None:
        candidate_dataset = []
        self.assertListEqual(candidate_dataset, [])

    def test_one_element_array(self) -> None:
        candidate_dataset = [1]
        self.assertListEqual(candidate_dataset, [1])

    def test_dummy_bubblesort(self) -> None:
        candidate_dataset = dummy_bubblesort(self.unsorted_dataset)
        self.assertListEqual(candidate_dataset, self.sorted_dataset)

    def test_classic_bubblesort(self) -> None:
        candidate_dataset = classic_bubblesort(self.unsorted_dataset)
        self.assertListEqual(candidate_dataset, self.sorted_dataset)

    def test_cocktail_bubblesort(self) -> None:
        candidate_dataset = cocktail_bubblesort(self.unsorted_dataset)
        self.assertListEqual(candidate_dataset, self.sorted_dataset)

    def test_comb_bubblesort(self) -> None:
        candidate_dataset = comb_bubblesort(self.unsorted_dataset)
        self.assertListEqual(candidate_dataset, self.sorted_dataset)
