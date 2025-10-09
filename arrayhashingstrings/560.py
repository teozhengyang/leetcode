# https://leetcode.com/problems/subarray-sum-equals-k/

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = {}
        prefix = 0
        counter[prefix] = 1
        result = 0

        for num in nums: 
            prefix += num
            difference = prefix - k 
            # add number of subarrays ending at current index with sum k (prefix - prev_prefix = k)
            result += counter.get(difference, 0)
            # update count of current prefix sum
            if prefix in counter: 
                counter[prefix] += 1
            else:
                counter[prefix] = 1
        
        return result
            