def check_input(func):
    def wrapper(arr):
        if arr is None:
            raise TypeError("Must be a list")
        if len(arr) < 2:
            return arr

        return func(arr)

    return wrapper


@check_input
def dummy_bubblesort(arr: list) -> list:
    do_sort = True
    while do_sort:
        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                do_sort = True
                break

            do_sort = False

    return arr


@check_input
def classic_bubblesort(arr: list) -> list:
    for j in range(len(arr)):
        for i in range(1, len(arr) - j):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]

    return arr


@check_input
def cocktail_bubblesort(arr: list) -> list:
    direction = 1
    begin = -1
    end = len(arr)
    while True:
        for i in range(begin + 2 * direction, end, direction):
            if direction > 0:
                if arr[i] < arr[i - 1]:
                    arr[i], arr[i - 1] = arr[i - 1], arr[i]
            else:
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]

        if direction > 0:
            begin, end = end - 1, begin
        else:
            begin, end = end + 1, begin
        direction = -direction

        if (begin >= end and direction > 0) or (end >= begin and direction < 0):
            break

    return arr


@check_input
def clear_fuzzy_bubblesort(arr: list) -> list:
    while True:
        odd_switch = False
        even_switch = False

        # odd loop
        for left_idx in range(0, len(arr), 2):
            right_idx = left_idx + 1
            if right_idx >= len(arr):
                break
            if arr[left_idx] > arr[right_idx]:
                arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
                odd_switch = True

        # even loop
        for left_idx in range(1, len(arr), 2):
            right_idx = left_idx + 1
            if right_idx >= len(arr):
                break
            if arr[left_idx] > arr[right_idx]:
                arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]
                even_switch = True

        if not odd_switch and not even_switch:
            break

    return arr


@check_input
def comb_bubblesort(arr: list) -> list:
    FACTOR = 1.247

    step = len(arr)
    while True:
        step = int(step // FACTOR)

        for left_idx in range(len(arr)):
            right_idx = left_idx + step
            if right_idx >= len(arr):
                break

            if arr[left_idx] > arr[right_idx]:
                arr[left_idx], arr[right_idx] = arr[right_idx], arr[left_idx]

        if step == 1:
            break

    return arr
