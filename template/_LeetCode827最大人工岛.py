from typing import List


class UnionFindSet:

    def __init__(self, dataList):
        self.parentDict = {}
        self.sizeDict = {}
        for item in dataList:
            self.addItem(item)

    def addItem(self, item):
        self.parentDict[item] = item
        self.sizeDict[item] = 1

    def find(self, item):  # find the root
        parent = self.parentDict[item]
        if item != parent:
            parent = self.find(parent)
        self.parentDict[item] = parent
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


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        N = len(grid)
        M = len(grid[0])

        def inBound(row, col):
            return 0 <= row < N and 0 <= col < M

        # convert grid into UnionFindSet
        dataList = []
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    dataList.append((i, j))
        UFSet = UnionFindSet(dataList)

        # all sea grid
        if not UFSet.parentDict:
            return 1

        #  four directions for neighbors of a grid, here only need two
        direct = [[0, 1], [1, 0]]
        # union land grids to form islands
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 0:
                    continue
                # else, encounter a land grid
                for d in direct:
                    # new row and new column
                    r = i + d[0]
                    c = j + d[1]
                    if inBound(r, c):
                        if grid[r][c] == 1:
                            UFSet.union((r, c), (i, j))

        MAX = max(UFSet.sizeDict.values())
        direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for i in range(N):
            for j in range(M):
                if grid[i][j] == 1:
                    continue
                # else, this is a sea grid we can fill
                islandDict = {}
                for d in direct:
                    r = i + d[0]
                    c = j + d[1]
                    if inBound(r, c):
                        if grid[r][c] == 1:
                            neighborIsland = UFSet.find((r, c))
                            if neighborIsland not in islandDict.keys():
                                islandDict[neighborIsland] = UFSet.sizeDict[neighborIsland]
                localmax = sum(islandDict.values()) + 1
                MAX = max(MAX, localmax)

        return MAX


# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#
#         N = len(grid)
#         M = len(grid[0])
#
#         def inBound(row, col):
#             return 0 <= row < N and 0 <= col < M
#
#         def dfs(i, j):
#             if not inBound(i, j):
#                 return 0
#             if grid[i][j] == 0:
#                 return 0
#
#             grid[i][j] = 0
#             myans = 1
#             for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
#                 r, c = i + x, j + y
#                 myans += dfs(r, c)
#             return myans
#
#         ans = 0
#         for i1 in range(N):
#             for j1 in range(M):
#                 ans = max(ans, dfs(i1, j1))
#         return ans


if __name__ == "__main__":
    obj = Solution()
    data = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,1,1,0,1,0,0,0,0,0,0,0,0],
            [0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,1,0,0],
            [0,0,0,0,0,0,0,1,1,1,0,0,0],
            [0,0,0,0,0,0,0,1,1,0,0,0,0]]

    # result = obj.maxAreaOfIsland(data)
    # print(result)








