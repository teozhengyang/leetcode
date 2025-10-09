# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        right = []
        count = 0

        for num in nums:
            if num == pivot:
                count += 1
            elif num < pivot:
                left.append(num)
            else:
                right.append(num)
        
        return left + [pivot] * count + right