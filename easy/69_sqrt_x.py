def mySqrt(self, x: int) -> int:
  left = 0
  right = x
  
  while left < right:
    mid = (left + right + 1) // 2 # add 1 to mid to avoid infinite loop when left == right - 1
    
    # if mid <= x // mid then target is in the right half
    if mid <= x // mid:
      left = mid
    else: # if mid > x // mid then target is in the left half
      right = mid - 1
  
  return left
