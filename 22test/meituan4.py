"""
BACKGROUND:
给定两个小于1000的整数，A, B
定义对X等于A或B可执行任意步以下三种操作：
opt1: X = X + 1
opt2: X = 2 * X
opt3: X = int(X/2)
输出把A和B变相等的最小操作步数
"""

import sys

SYSMAX = sys.maxsize

mystr = input().split(" ")

A, B = int(mystr[0]), int(mystr[1])

if A == B:
    print(0)
else:
    # treat A as the larger number
    if B > A: # exchange the value
        temp = A
        A = B
        B = temp

    # A always > B
    table = []  # A * B table recording sub problem answer
    # only table[i][j] that i > j and i < 2A + 1 are defined
    for ctr in range(2 * A + 1):
        row = [-1 for _ in range(ctr)]
        table.append(row)
    table[1][0] = 1
    # print(table)

    def solution(a, b):
        # print("!!!!! in ", a, b)
        if a == b:
            return 0
        if a < b:  # swap the value
            temp1 = a
            a = b
            b = temp1
        # hereafter, a is promised to > b.
        if a > 2 * A:  # unavailable solution
            return SYSMAX

        if table[a][b] != -1:
            return table[a][b]

        table[a][b] = SYSMAX - 10  # block this value to prevent subroutine going into infinite loop

        if a - b == 1:
            ans = 1
        else:
            s1 = a - b
            s2 = solution(int(a / 2), b) + 1
            s3 = solution(a, 2 * b) + 1
            ans = min(s1, s2, s3)
        table[a][b] = ans
        return ans

    mysolution = solution(A, B)
    print(mysolution)

