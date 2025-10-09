# https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            # get the max height between the two pointers
            max_height = min(height[left], height[right])
            # update area if the current area is larger
            area = max((right - left) * max_height, area)
            # move left pointer if left height is smaller or equal to right height
            if height[left] <= height[right]:
                left += 1
            else: # move right pointer if right height is smaller than left height 
                right -= 1
        
        return area