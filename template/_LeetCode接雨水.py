from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        SUM = 0
        length = len(height)
        if length < 3:
            return 0  # only when length >= 3 it is possible to contain some water
        
        max_left = [0] * length
        max_right = [0] * length

        max_left[0] = height[0]
        for i in range(1, length):
            max_left[i] = max(max_left[i-1], height[i-1])

        max_right[length-1] = height[length-1]
        for i in range(length-2, -1, -1):
            max_right[i] = max(max_right[i+1], height[i+1])

        # print(max_left)
        # print(max_right)

        for i in range(1, length-1):
            MIN = min(max_left[i], max_right[i])
            if MIN > height[i]:
                SUM += (MIN - height[i])
        return SUM

    # refine the space complexity:
    #
    # 只要两个变量来存max_left 和 max_right
    # height [ left - 1] 是可能成为 max_left 的变量， 同理，height [ right + 1 ] 是可能成为 right_max 的变量。
    #
    # 只要保证 height [ left - 1 ] < height [ right + 1 ] ，那么 max_left 就一定小于 max_right。
    #
    # 上述情况下从左往右算，反之从右往左算。
    #

    def trap2(self, height: List[int]) -> int:
        SUM = 0
        length = len(height)
        if length < 3:
            return 0  # only when length >= 3 it is possible to contain some water

        max_left = 0
        max_right = 0
        lptr = 1
        rptr = length - 2

        for i in range(1, length - 1):
            if height[lptr-1] <= height[rptr+1]:
                max_left = max(max_left, height[lptr-1])
                MIN = max_left
                if MIN > height[lptr]:
                    SUM += (MIN - height[lptr])
                lptr += 1
            else:
                max_right = max(max_right, height[rptr+1])
                MIN = max_right
                if MIN > height[rptr]:
                    SUM += (MIN - height[rptr])
                rptr -= 1

        return SUM


if __name__ == "__main__":
    obj = Solution()
    print(obj.trap2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

