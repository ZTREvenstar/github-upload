def quicksort(seq, i, j):
    if i >= j:
        return seq

    mid = partition(seq, i, j)
    quicksort(seq, i, mid - 1)
    quicksort(seq, mid + 1, j)
    return seq


def quicksortFindKLargest(seq, K):
    length = len(seq)
    low = 0
    high = length - 1
    # index is the mid
    index = partition(seq, low, high)
    while index != length - K:
        if index < length - K:
            low = index + 1
            index = partition(seq, low, high)
        else:
            high = index - 1
            index = partition(seq, low, high)
    return seq[index]


def partition(seq, i, j):

    pivot = seq[i]
    while i < j:
        while i < j and seq[j] >= pivot:
            j -= 1
        seq[i] = seq[j]
        while i < j and seq[i] <= pivot:
            i += 1
        seq[j] = seq[i]
    seq[j] = pivot

    # i == j, is mid
    return i


if __name__ == "__main__":
    lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]
    print("排序前的序列为：")
    print(lists)
    anotherLists = lists[:]
    print("排序后的序列为：")
    print(quicksort(anotherLists, 0, len(anotherLists)-1))
    print(quicksortFindKLargest(lists, 3))



