# 路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。
# 同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
# 路径和 是路径中各节点值的总和。
# 给你一个二叉树的根节点 root ，返回其 最大路径和

# 分别往左右leaf递归。考虑一个node，知道左，知道右，值回传，但以该node为root的path通过对比全局最大来计算

import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:

        globalMax = [-(sys.maxsize - 100)]

        def dfs(node: TreeNode) -> int:
            #  返回值为一条路径（并非直接答案）：该路径有如下限制：一端是根（node）。
            leftSum, rightSum = 0, 0
            if root.left is not None:
                leftSum = dfs(node.left)
            if root.right is not None:
                rightSum = dfs(node.right)

            if max(leftSum, 0) + max(rightSum, 0) + root.val > globalMax[0]:
                globalMax[0] = max(leftSum, 0) + max(rightSum, 0) + root.val

            return root.val + max(max(leftSum, 0), max(rightSum, 0))

        dfs(root)  # dfs会把所有node 按左右中顺序都算一次，暴搜

        return globalMax[0]
