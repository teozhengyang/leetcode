# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/

from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # empty prefix = 0 so even count starts at 1
        even = 1
        odd = 0
        result = 0
        prefix = 0
        
        for num in arr:
            prefix += num
            # add number of odd subarrays ending at current index for even prefix
            if prefix % 2 == 0:
                result += odd
                even += 1
            # odd number of even subarrays ending at current index for odd prefix
            else:
                result += even
                odd += 1
        
        return result % (10**9 + 7)