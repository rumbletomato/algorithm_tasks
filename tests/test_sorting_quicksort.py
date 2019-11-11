import random
from unittest import TestCase

from atasks.sorting.quicksort import quicksort


class TestSortingQuicksort(TestCase):
    DATASET_LENGTH = 10000
    MIN_VALUE = -99
    MAX_VALUE = 99

    def setUp(self) -> None:
        super().setUp()

        self.unsorted_dataset = [random.randrange(self.MIN_VALUE, self.MAX_VALUE) for _ in range(self.DATASET_LENGTH)]
        self.sorted_dataset = sorted(self.unsorted_dataset)

    def test_quicksort(self):
        candidate_dataset = quicksort(self.unsorted_dataset, 0, len(self.unsorted_dataset) - 1)
        self.assertListEqual(candidate_dataset, self.sorted_dataset)
