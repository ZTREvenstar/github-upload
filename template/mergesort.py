def mergesort(seq):
    if len(seq) <= 1:
        return seq
    # mid is the index of mid item
    mid = len(seq) // 2
    left = mergesort(seq[:mid])
    # print(left)
    right = mergesort(seq[mid:])
    # print(right)
    return merge(left, right)


def merge(left, right):
    temp = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            temp.append(left[i])
            i += 1
        else:
            temp.append(right[j])
            j += 1
    temp += left[i:]
    temp += right[j:]
    return temp


seq = [0, 5, 7, 6, 8, 7, 5, 2, 1, 3, 1, 5]
print("before:   ", end='')
print(seq)
seq = mergesort(seq)
print("after:   ", end='')
print(seq)
