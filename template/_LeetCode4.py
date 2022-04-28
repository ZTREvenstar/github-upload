from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        len1 = len(nums1)
        len2 = len(nums2)
        LEN = len1 + len2

        def getKthElement(k):
            index1, index2 = 0, 0
            while True:
                if index1 == len1:
                    return nums2[index2 + k - 1]
                if index2 == len2:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                newIndex1 = min(index1 + k // 2 - 1, len1 - 1)
                newIndex2 = min(index2 + k // 2 - 1, len2 - 1)

                pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
                if pivot1 <= pivot2:
                    k -= newIndex1 - index1 + 1
                    index1 = newIndex1 + 1
                else:
                    k -= newIndex2 - index2 + 1
                    index2 = newIndex2 + 1

        if LEN % 2 == 1:
            return getKthElement((LEN + 1) // 2)
        else:
            return ( getKthElement(LEN // 2) + getKthElement(LEN // 2 + 1) ) / 2
