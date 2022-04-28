from typing import List


class Solution:
    def isMatch(self, a_s: str, b_p: str) -> bool:
        if a_s == "":
            if b_p == "":
                return True
            for i in b_p:
                if i != "*":
                    return False
            return True
        if b_p == "":
            return a_s == ""
        len1 = len(a_s)
        len2 = len(b_p)

        def matches(a, b) -> bool:
            if a < 0 and b == 0 and b_p[b] == "*":
                return True
            if a < 0 or b < 0:
                return False
            return f[a][b]

        # initialize the table
        f = [[False] * len2 for _ in range(len1)]

        # start dynamic programming
        if b_p[0] == a_s[0] or b_p[0] == "?" or b_p[0] == "*":
            f[0][0] = True

        for i in range(len1):
            for j in range(len2):
                if i == 0 and j == 0:
                    continue
                if b_p[j] == "*":
                    f[i][j] = matches(i, j-1) or matches(i-1, j-1) or matches(i-1, j)
                elif b_p[j] == "?" or b_p[j] == a_s[i]:
                    f[i][j] = matches(i-1, j-1)

        return f[len1-1][len2-1]


if __name__ == "__main__":
    obj = Solution()
    # data = [0,0,0,0,0,0,0,0,1]
    # target = 1
    result = obj.isMatch("ho", "**ho")
    print(result)

# "acdcb" "a*c?b"
# "aab" "c*a*b"

# 现在只需解决p前任意个*啥都不匹配的问题
