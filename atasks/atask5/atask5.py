def get_closest_part_sum_idx(part_sums, target_value):
    left_idx = 0
    right_idx = len(part_sums) - 1

    while right_idx - left_idx > 1:
        middle_idx = int((right_idx + left_idx) // 2)
        if target_value <= part_sums[middle_idx]:
            right_idx = middle_idx
        elif target_value > part_sums[middle_idx]:
            left_idx = middle_idx

    return right_idx


def search_consecutive_set_of_numbers(arr: list, target_sum: int):
    start_idx: int = 0
    end_idx: int = 0

    partial_sum: int = 0
    all_partial_sums = [0]
    for idx, elem in enumerate(arr):
        partial_sum += elem
        all_partial_sums.append(all_partial_sums[-1] + elem)

        if (partial_sum > target_sum):
            # so binary search
            diff = partial_sum - target_sum
            # N logN
            partial_sum_idx = get_closest_part_sum_idx(all_partial_sums, diff)
            partial_sum -= all_partial_sums[partial_sum_idx]
            start_idx += partial_sum_idx

        if partial_sum == target_sum:
            return [start_idx, end_idx]

        end_idx += 1

    return "Sum was not found"
