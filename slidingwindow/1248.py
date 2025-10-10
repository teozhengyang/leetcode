# https://leetcode.com/problems/count-number-of-nice-subarrays/

from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Dictionary to store frequency of odd counts
        freq_odd = {0: 1}
        num_odds = 0
        result = 0

        for num in nums:
            # Increment odd count if the number is odd
            if num % 2 != 0:
                num_odds += 1
            # Calculate the difference needed to form a valid subarray
            difference = num_odds - k
            # update result if the difference exists in freq_odd
            if difference in freq_odd:
                result += freq_odd[difference] 
            # Update the frequency of the current odd count
            if num_odds in freq_odd:
                freq_odd[num_odds] += 1
            else:
                freq_odd[num_odds] = 1
        
        return result
