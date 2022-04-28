from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length = len(nums)

        AbsSum = 0
        for i in nums:
            AbsSum += abs(i)

        current_dp = [0] * (2 * AbsSum + 1)
        current_dp[nums[0] + AbsSum] = 1
        current_dp[-nums[0] + AbsSum] = 1

        for i in range(1, length):
            next_dp = [0] * (2 * AbsSum + 1)
            for sum in range(-AbsSum, AbsSum + 1):
                if current_dp[sum + AbsSum] > 0:
                    next_dp[sum + nums[i] + AbsSum] += current_dp[sum + AbsSum]
                    next_dp[sum - nums[i] + AbsSum] += current_dp[sum + AbsSum]
            current_dp = next_dp

        return current_dp[target + AbsSum] if AbsSum >= target >= -AbsSum else 0
