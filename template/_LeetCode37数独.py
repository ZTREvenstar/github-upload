from typing import List, Tuple


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        Set_comp = set("123456789")
        GRID_AV = []
        ROW_AV = []
        COL_AV = []
        # initialize tables of available
        for i in range(9):
            GRID_AV.append(Set_comp.copy())
            ROW_AV.append(Set_comp.copy())
            COL_AV.append(Set_comp.copy())
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n == ".":
                    continue
                index = 3 * (i // 3) + j // 3
                GRID_AV[index].discard(n)
                ROW_AV[i].discard(n)
                COL_AV[j].discard(n)

        # used for dfs to traverse each grid
        def next(row, col) -> Tuple[int, int]:
            if row > 8 or col > 8:
                print("error!!!!!")
                return -1, -1
            elif col == 8:
                return row + 1, 0
            else:
                return row, col + 1

        end_dfs = [0]

        def dfs(r, c):
            if r == 9 and c == 0:
                end_dfs[0] = 1
                print("@2222222")
                return

            if board[r][c] == ".":
                index = 3 * (r // 3) + c // 3
                set_av = GRID_AV[index] & ROW_AV[r] & COL_AV[c]
                if not set_av:
                    return
                for e in set_av:

                    GRID_AV[index].discard(e)
                    ROW_AV[r].discard(e)
                    COL_AV[c].discard(e)
                    board[r][c] = e
                    NEXT = next(r, c)

                    dfs(NEXT[0], NEXT[1])

                    if end_dfs[0] == 1:
                        return

                    # restore the state
                    board[r][c] = "."
                    GRID_AV[index].add(e)
                    ROW_AV[r].add(e)
                    COL_AV[c].add(e)
            else:
                NEXT = next(r, c)
                dfs(NEXT[0], NEXT[1])

            return

        dfs(0, 0)
        print("Aaaaaaaaa")


if __name__ == "__main__":
    obj = Solution()
    data = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    obj.solveSudoku(data)
    #print(result)
