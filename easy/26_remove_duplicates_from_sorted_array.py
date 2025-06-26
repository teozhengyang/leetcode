from typing import List

def removeDuplicates(self, nums: List[int]) -> int:
  # counter for unique elements
  k = 0
  
  # loop through array
  for num in nums:
    # if first element or not equal to previous element, add to unique elements
    if k == 0 or num != nums[k - 1]:
      nums[k] = num
      k += 1

  # return the length of unique elements
  return k