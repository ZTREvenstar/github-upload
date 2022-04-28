"""
4
0011

7
1000101
"""

n = int(input())

string = input()
statusList = [int(i) for i in string]

# print(statusList)

# left should attack, right should defensee

# initialization. Start traversing from left to right
W = 0
V = 0
for i in range(0, n):
    f = statusList[i]
    if f == 0:  # can only attack
        pass
    else:  # f == 1  # can only defense
        V += i + 1

# init: pos = 0
ans = abs(W - V)

for index in range(0, n):
    # add fighter with index into W
    f = statusList[index]
    if f == 0:
        W += index + 1
    else:
        V -= (index + 1)

    temp = abs(W - V)
    if temp < ans:
        ans = temp

print(ans)
