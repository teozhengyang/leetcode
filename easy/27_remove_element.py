from typing import List


def removeElement(self, nums: List[int], val: int) -> int:
  # counter for elements not equal to val
  k = 0
  
  # loop through array
  for num in nums:
    # if the number is not equal to val, add it to the new array and increment k
    if num != val:
      nums[k] = num
      k += 1
      
  return k