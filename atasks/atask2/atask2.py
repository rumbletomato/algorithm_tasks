from operator import itemgetter
from typing import List, Optional


def merge_two(first: List[int], second: List[int]) -> Optional[List[int]]:
    if first[1] >= second[0]:
        return [first[0], second[1]]
    return None


def merge_intervals(intervals: list) -> list:
    intervals.sort(key=itemgetter(0))

    merged_intervals = []
    last_merge_result = intervals[0]
    for i in range(1, len(intervals)):
        result = merge_two(last_merge_result, intervals[i])
        if result is None:
            merged_intervals.append(last_merge_result)
            last_merge_result = intervals[i]
        else:
            last_merge_result = result

    merged_intervals.append(last_merge_result)

    return merged_intervals
