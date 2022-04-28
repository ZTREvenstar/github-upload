from typing import List


def binary_search(array: List[int], num: int) -> int:
    # return index i where array[i] <= num and array[i+1] > num
    l = 0
    r = len(array) - 1
    location = r
    while l <= r:
        mid = (l + r) // 2
        if array[mid] > r:
            r = mid - 1
            location = r
        else:
            l = mid + 1
    return location
