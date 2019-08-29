def clever_sort(already_sorted: list, unsorted: list) -> list:
    return sorted(unsorted, key=lambda x: already_sorted.index(x))
