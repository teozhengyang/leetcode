# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 2
        # start from the third number
        for i in range(2, len(nums)):
            # compare with the number two places before
            if (nums[i] != nums[counter - 2]):
                # add new number to the counter position
                nums[counter] = nums[i]
                counter += 1
        return counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_num = nums[0]
        count = 1
        k = 1

        for i in range(1, len(nums)):
            # same value
            if curr_num == nums[i]:
                count += 1
                # allow at most two duplicates
                if count <= 2:
                    nums[k] = nums[i]
                    k += 1
            # different value
            else:
                # reset count, update curr_num
                nums[k] = nums[i]
                curr_num = nums[i]
                count = 1
                k += 1

        return k     