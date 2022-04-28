class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        len1 = len(s)
        len2 = len(p)

        def matches(a, b) -> bool:
            if a < 0 or b < 0:
                return False
            return f[a][b]

        # initialize the table
        f = [[False] * len1 for _ in range(len2)]

        # start dynamic programming
        if p[0] == s[0] or p[0] == "?" or p[0] == "*":
            f[0][0] = True

        for i in range(len1):
            for j in range(len2):
                if i == 0 and j == 0:
                    continue
                if p[j] == "*":
                    f[i][j] = matches(i, j-1) or matches(i-1, j-1) or matches(i-1, j)
                elif p[j] == "?" or p[j] == s[i]:
                    f[i][j] = matches(i-1, j-1)

        return f[len1-1][len2-1]
