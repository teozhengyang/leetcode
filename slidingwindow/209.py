# https://leetcode.com/problems/minimum-size-subarray-sum/

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = 0
        left = 0
        result = float('inf')

        for i in range(len(nums)):
            # update current sum
            curr_sum += nums[i]
            # shrink window while curr_sum more than or equal to target
            while curr_sum >= target:
                # update result to minimum length found
                result = min(result, i - left + 1)
                curr_sum -= nums[left]
                left += 1
        
        return result if result != float('inf') else 0