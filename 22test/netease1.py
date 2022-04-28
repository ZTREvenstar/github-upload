"""
123456
456123
234561
561234
345612
612345
"""

"""
251634
634251
526143
143526
312465
465312
"""

"""
152634
634152
516243
243516
321465
465321
"""


n = int(input())

# print(n)

ans = 0

for i in range(0, n):
    # init grid
    grid = []
    for j in range(0, 6):
        row = []
        string = input()
        for k in range(0, 6):
            row.append(int(string[k]))
        grid.append(row)
    #print(grid)

    outer_skip_flag = 0
    # check validity
    # rows
    for r in grid:
        my_dict = [0, 0, 0, 0, 0, 0]
        inner_skip_flag = 0
        for num in r:
            if inner_skip_flag:
                break
            if my_dict[num - 1] == 0:
                my_dict[num - 1] = 1
            else:
                outer_skip_flag = 1
                inner_skip_flag = 1

    if outer_skip_flag:
        continue
    # cols
    for col in range(0, 6):
        my_dict = [0, 0, 0, 0, 0, 0]
        inner_skip_flag = 0
        for row in range(0, 6):
            if inner_skip_flag:
                break
            num = grid[row][col]
            if my_dict[num - 1] == 0:
                my_dict[num - 1] = 1
            else:
                outer_skip_flag = 1
                inner_skip_flag = 1

    if outer_skip_flag:
        continue
    # gongs
    for n in range(0, 6):
        my_dict = [0, 0, 0, 0, 0, 0]
        inner_skip_flag = 0
        x = (n // 2) * 2  # x = 0, 2, 4
        y = (n % 2) * 3  # y' = 0, 3,
        my_list = [grid[x][y], grid[x][y+1], grid[x][y+2], grid[x+1][y], grid[x+1][y+1], grid[x+1][y+2]]
        # print(my_list)
        for num in my_list:
            if inner_skip_flag:
                break
            if my_dict[num - 1] == 0:
                my_dict[num - 1] = 1
            else:
                outer_skip_flag = 1
                inner_skip_flag = 1

    if not outer_skip_flag:
        ans += 1
    # print("!!!!", outer_skip_flag)
print(ans)


