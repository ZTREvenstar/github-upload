"""
股票买卖问题，
一共有n天，知道以后每一天的股价，一开始有m元
每天可以不买或者买进一只或者卖出一只
求在第n天结束时可能获得的最大资产：当天股价*手上股票数量+手上钱数
"""

"""
6 2
2 3 1 1 1 2

3 2
1 1 4
"""

myinput = input().split(" ")
n, m = int(myinput[0]), int(myinput[1])

myinput = input().split(" ")
price = map(lambda x: int(x), myinput)

# the answer at the end of the kth day
def solution(k, mm, xx):
    if k == n:
        return price[n-1] * xx + mm

    solution(k+1, )

