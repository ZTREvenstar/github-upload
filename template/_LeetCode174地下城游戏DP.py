from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        M = len(dungeon)
        N = len(dungeon[0])
        INF = int(1e6)
        table = [[INF] * N for _ in range(M)]  # table: record the min before HP in each cell
        print(table)
        # initialize the destination HP>=1
        if dungeon[M-1][N-1] < 0:
            table[M-1][N-1] = 1 - dungeon[M-1][N-1]
        else:
            table[M-1][N-1] = 1

        # look up to the table. from right bottom to left upper.
        for j in range(N-1, -1, -1):
            for i in range(M-1, -1, -1):
                if j == N-1 and i == M-1:
                    continue
                # construct from sub problem
                if i + 1 < M:
                    table[i][j] = min(table[i+1][j], table[i][j])
                if j + 1 < N:
                    table[i][j] = min(table[i][j+1], table[i][j])
                # consider the update inside grid
                table[i][j] = max(table[i][j] - dungeon[i][j], 1)

        return table[0][0]


if __name__ == "__main__":

    obj = Solution()
    result = obj.calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])
    print(result)
