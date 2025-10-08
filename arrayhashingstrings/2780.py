# https://leetcode.com/problems/minimum-index-of-a-valid-split/

from collections import Counter
from typing import List

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        left_map = Counter()
        right_map = Counter(nums)

        for i, num in enumerate(nums):
            # add to left map
            if num in left_map:
                left_map[num] += 1
            else:
                left_map[num] = 1
            # remove from right map
            right_map[num] -= 1

            # check if left and right have dominator
            if left_map[num] > ((i + 1) // 2) and right_map[num] > ((len(nums) - i - 1) // 2):
                return i
        
        return -1