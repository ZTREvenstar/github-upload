class MinHeap:
    def __init__(self):
        self.dataList = []

    def getParentIndex(self, index):
        if index <= 0 or index > len(self.dataList) - 1:
            return None
        else:
            return (index - 1) >> 1  # equivalent to (index - 1) // 2

    def swap(self, index_a, index_b):
        self.dataList[index_a], self.dataList[index_b] = self.dataList[index_b], self.dataList[index_a]

    def insert(self, data):
        self.dataList.append(data)
        index = len(self.dataList) - 1
        parent = self.getParentIndex(index)
        while parent is not None and self.dataList[parent] > self.dataList[index]:
            self.swap(parent, index)
            index = parent
            parent = self.getParentIndex(parent)

    def pop(self):
        removed = self.dataList[0]
        temp = self.dataList.pop(-1)
        if len(self.dataList) != 0:
            self.dataList[0] = temp
            self.heapify(0)
        return removed

    def heapify(self, index):
        indexmax = len(self.dataList) - 1
        while True:
            small = index
            if 2 * index + 1 <= indexmax and self.dataList[small] > self.dataList[2 * index + 1]:
                small = 2 * index + 1
            if 2 * index + 2 <= indexmax and self.dataList[small] > self.dataList[2 * index + 2]:
                small = 2 * index + 2
            if index == small:
                break
            self.swap(index, small)
            index = small


if __name__ == "__main__":
    myMinHeap = MinHeap()
    myMinHeap.insert(0)
    myMinHeap.insert(4)
    myMinHeap.insert(33)
    myMinHeap.insert(2)
    myMinHeap.insert(6)
    myMinHeap.insert(999)

    for i in range(6):
        print(myMinHeap.pop())


