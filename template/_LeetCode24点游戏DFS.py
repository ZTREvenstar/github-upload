from typing import List


class Solution:

    def judgePoint(self, nums: List[int]) -> bool:
        GOAL = 24
        threshold = 1e-6
        ADD, MULTIPLY, SUBTRACT, DIVIDE = 0, 1, 2, 3

        def solve(nums: List[float]) -> bool:
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - GOAL) < threshold

            for index1, num1 in enumerate(nums):
                for index2, num2 in enumerate(nums):
                    # 抓取任意两个数字组成新数字
                    if index1 == index2:
                        continue

                    newNums = list()

                    # add all remaining numbers into the new list
                    for index3, num3 in enumerate(nums):
                        if index3 != index1 and index3 != index2:
                            newNums.append(num3)
                    for i in range(4):
                        if i < 2 and index1 > index2:  # addition and multiplication are symmetric
                            continue
                        if i == ADD:
                            newNums.append(num1 + num2)
                        elif i == MULTIPLY:
                            newNums.append(num1 * num2)
                        elif i == SUBTRACT:
                            newNums.append(num1 - num2)
                        elif i == DIVIDE:
                            if abs(num2) < threshold:
                                continue
                            newNums.append(num1 / num2)
                        if solve(newNums):
                            return True
                        newNums.pop()
            return False

        return solve(nums)

