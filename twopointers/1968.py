# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # wiggle sort
        for i in range(len(nums) - 1):
            # smaller element in even index OR bigger element in odd index (small -> big -> small)
            if (i % 2 == 0 and nums[i] > nums[i + 1]) or (i % 2 == 1 and nums[i] < nums[i + 1]):
                temp = nums[i]
                nums[i] = nums[i + 1]
                nums[i + 1] = temp

        return nums