from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        length = len(envelopes)
        if length == 0:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # initialize
        dp = [envelopes[0][1]]
        for i in range(1, length):
            n = envelopes[i][1]
            if n > dp[-1]:
                dp.append(n)
            else:
                # start binary search to find the corresponding index
                l = 0
                r = len(dp)
                mid = r
                while l <= r:
                    mid = (l + r) // 2
                    if dp[mid] >= n:
                        r = mid - 1
                    else:
                        l = mid + 1
                dp[mid + 1] = n

        return len(dp)
