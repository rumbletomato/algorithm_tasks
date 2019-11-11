def quicksort(arr: list, low_idx: int, high_idx: int) -> list:
    def partition(arr: list, low_idx: int, high_idx: int) -> int:
        pivotal = arr[high_idx]
        i = low_idx

        for j in range(low_idx, high_idx):
            if arr[j] < pivotal:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[high_idx] = arr[high_idx], arr[i]

        return i

    if low_idx < high_idx:
        pivotal_idx = partition(arr, low_idx, high_idx)
        quicksort(arr, low_idx, pivotal_idx - 1)
        quicksort(arr, pivotal_idx + 1, high_idx)

    return arr
