class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # stack存index number，确定valid/invalid
        # 也可强行DP，分两种情况
        return 1