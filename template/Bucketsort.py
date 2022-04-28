def Bucketsort(array, num):

    max, min = max(array), min(array)

    bucketSize = int((max - min +1) / num)
    bucket = [[] for _ in range(num)]

    for item in array:
        bucket[int((item - min) / bucketSize)].append(item)

    result = []
    for i in range(0, len(bucket)):
        result += sorted(bucket[i])

    return result