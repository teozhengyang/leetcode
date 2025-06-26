from typing import List

def searchInsert(self, nums: List[int], target: int) -> int:
  left = 0
  right = len(nums)
  
  # Binary search to find the insert position
  while left < right:
    mid = (left + right) // 2
    
    # target in right half
    if nums[mid] < target:
      left = mid + 1
    # target in left half or is equal to mid
    else:
      right = mid
  
  return left