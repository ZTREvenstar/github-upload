from typing import List


# 从边开始的dfs   判断要不要进入递归在父函数内完成，因此停止递归控制更加简单
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        M = len(heights)
        N = len(heights[0])

        table = [[0] * N for _ in range(M)]
        # -1: unvisited. 0: can not go to both. 1: can go to P. 2: can go to A. 3: can go to both
        solution = []

        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):  # check P
            if table[r][c] == 1:
                return
            table[r][c] = 1
            for d in direction:
                row, col = r + d[0], c + d[1]
                if 0 < row < M and 0 < col < N and heights[r][c] <= heights[row][col]:
                    dfs(row, col)

        def dfs2(r, c):  # check A
            if table[r][c] == 2 or table[r][c] == 3:
                return
            table[r][c] += 2
            if table[r][c] == 3:
                solution.append([r, c])

            for d in direction:
                row, col = r + d[0], c + d[1]
                # print(0 < row < M and 0 < col < N and heights[r][c] <= heights[row][col])
                if 0 <= row < M and 0 <= col < N and heights[r][c] <= heights[row][col]:
                    dfs2(row, col)

        for i in range(M):
            dfs(i, 0)
        for j in range(N):
            dfs(0, j)
        for i in range(M):
            dfs2(i, N - 1)
        for j in range(N):
            dfs2(M - 1, j)
        return solution


if __name__ == "__main__":
    # obj = Solution()
    # data = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    # result = obj.pacificAtlantic(data)
    # result.sort(key=lambda x: (x[0], x[1]))
    print("1" * 5)
