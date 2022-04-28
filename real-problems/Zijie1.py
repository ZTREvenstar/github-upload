# index starts from 0
def getChild(selfindex: int, option: str):
    if option == "left":
        if 2 * selfindex + 1 < N:
            return 2 * selfindex + 1
        else:
            return -1
    if option == "right":
        if 2 * selfindex + 2 < N:
            return 2 * selfindex + 2
        else:
            return -1


# 9
# 5194 34 91 51 72 46 12 9812 6054

N = int(input())

Tree = input()
Tree = Tree.split(" ")

# build the tree
for i in range(len(Tree)):
    Tree[i] = int(Tree[i])

# print(type(Tree[0]))

# 用dfs求最大：
# 已知左子树答案， 已知右子树答案
# 若左右子树的根都没选，直接两个加自己的根就是答案
# 若左右存在选了根的情况，则对比   有所有子根但没自己    和  有所有非子根但有自己

# the final answer, recursion shall check this with its answer
ANS = [0]


# 返回tuple， 第一个是ans，第二个代表自己的根有没有选过
def dfs(index: int):
    if index == -1:
        return 0, 0

    myleft = getChild(index, "left")
    myright = getChild(index, "right")

    # if myleft >= N:  # 越界
    #     if ANS[0] < Tree[index]:
    #         ANS[0] = Tree[index]
    #     return Tree[index], 1  # 0 for 没选自己根，1 for 选了自己根

    leftans, leftR = dfs(myleft)
    rightans, rightR = dfs(myright)

    if leftR == 0 and rightR == 0:
        ans = leftans + rightans + Tree[index]
        if ANS[0] < ans:
            ANS[0] = ans
        return ans, 1
    elif leftR == 1 and rightR == 0:
        ans1 = leftans + rightans
        sub1, _ = dfs(getChild(myleft, "left"))
        sub2, _ = dfs(getChild(myleft, "right"))
        ans2 = sub1 + sub2 + rightans + Tree[index]
        if ans1 > ans2:
            if ANS[0] < ans1:
                ANS[0] = ans1
            return ans1, 0
        else:
            if ANS[0] < ans2:
                ANS[0] = ans2
            return ans2, 1
    elif leftR == 0 and rightR == 1:
        ans1 = leftans + rightans
        sub1, _ = dfs(getChild(myright, "left"))
        sub2, _ = dfs(getChild(myright, "right"))
        ans2 = sub1 + sub2 + leftans + Tree[index]
        if ans1 > ans2:
            if ANS[0] < ans1:
                ANS[0] = ans1
            return ans1, 0
        else:
            if ANS[0] < ans2:
                ANS[0] = ans2
            return ans2, 1
    else:
        ans1 = leftans + rightans
        sub1, _ = dfs(getChild(myleft, "left"))
        sub2, _ = dfs(getChild(myleft, "right"))
        sub3, _ = dfs(getChild(myright, "left"))
        sub4, _ = dfs(getChild(myright, "right"))
        ans2 = sub1 + sub2 + sub3 + sub4 + Tree[index]
        if ans1 > ans2:
            if ANS[0] < ans1:
                ANS[0] = ans1
            return ans1, 0
        else:
            if ANS[0] < ans2:
                ANS[0] = ans2
            return ans2, 1


dfs(0)
print(ANS[0])
