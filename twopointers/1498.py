# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

from typing import List

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # order does not matter (only values in subsequences do)
        nums.sort()
        left = 0
        right = len(nums) - 1
        result = 0

        while left <= right:
            # valid section
            if nums[left] + nums[right] <= target:
                # pick/don't pick element in between
                result += pow(2, right - left, 10**9 + 7)
                left += 1
            # lower sum to reach target
            else:
                right -= 1
        
        return result % (10**9 + 7)
