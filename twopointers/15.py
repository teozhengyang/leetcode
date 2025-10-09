# https://leetcode.com/problems/3sum/

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort
        nums.sort()

        results = []

        for i in range(len(nums) - 2):
            # skip same nums as previous num
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            else:
                # start and end pointers per num
                start = i + 1
                end = len(nums) - 1
                # loop through to find valid triplets
                while start < end:
                    total = nums[i] + nums[start] + nums[end]
                    # valid triplets
                    if total == 0:
                        results.append([nums[i], nums[start], nums[end]])
                        start += 1
                        end -= 1
                        # advance start num to new num
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1
                        # shrink end num to new num
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
                    # advance start num
                    elif total < 0:
                        start += 1
                    # shrink end num
                    else:
                        end -= 1
        
        return results
                