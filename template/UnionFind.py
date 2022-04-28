class UnionFindSet:

    def __init__(self, dataList):
        self.parentDict = {}
        self.sizeDict = {}

        # initialize. All nodes are separate
        for node in dataList:
            self.parentDict[node] = node
            self.sizeDict[node] = 1

    # return the root of the node
    def find(self, node):
        parent = self.parentDict[node]
        if node != parent:
            parent = self.find(parent)
        # path compression
        self.parentDict[node] = parent
        return parent

    def inSameSet(self, a, b):
        return self.find(a) == self.find(b)

    def union(self, a, b):
        if a is None or b is None:
            return
        aRoot = self.find(a)
        bRoot = self.find(b)

        if aRoot != bRoot:
            aSize = self.sizeDict[aRoot]
            bSize = self.sizeDict[bRoot]

            if aSize <= bSize:
                self.parentDict[aRoot] = bRoot
                self.sizeDict.pop(aRoot)
                self.sizeDict[bRoot] = aSize + bSize
            else:
                self.parentDict[bRoot] = aRoot
                self.sizeDict.pop(bRoot)
                self.sizeDict[aRoot] = aSize + bSize


if __name__ == '__main__':
    nodes = ['剑魂', '红眼', '漫游', '元素', '魔道', '战法', '大枪', '散打', '弹药', '机械']
    union_find = UnionFindSet(nodes)
    union_find.union('剑魂', '红眼')
    union_find.union('漫游', '大枪')
    union_find.union('漫游', '弹药')
    union_find.union('漫游', '机械')
    union_find.union('元素', '魔道')
    union_find.union('元素', '战法')

    print(union_find.inSameSet('大枪', '弹药'))  # True
    print(union_find.inSameSet('剑魂', '战法'))  # False
    print(union_find.inSameSet('魔道', '散打'))  # False
    print(union_find.inSameSet('魔道', '战法'))  # True



