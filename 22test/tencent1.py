"""
3
0123
1234
2345

4
0000
0101
1011
0111
"""


n = int(input())

grid = []
for i in range(0, n):
    row = input()
    grid.append(row)

# have 10^5 numbers at most, each number is 10^8 at most

# read all numbers into mylist now.
mylist = []

l = len(grid[0])

for i in range(0, l):
    temp = ""
    meetnonzero = 0
    for j in range(0, n):
        if grid[j][i] == '0' and meetnonzero == 0:
            # precedent zeros
            continue
        if grid[j][i] != '0' and meetnonzero == 0:
            # encounter first nonzero number
            meetnonzero = 1
        temp = temp + grid[j][i]

    if temp == "":
        mylist.append(0)
    else:
        temp = int(temp)
        mylist.append(temp)

mylist.sort()

# print:
for i in range(0, l):
    print(mylist[i], end='')
    if i != l - 1:
        print(" ", end='')








