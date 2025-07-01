def climbStairs(self, n: int) -> int:
  prev = 0
  # 1 way to reach current step when n == 0
  curr = 1
  
  for _ in range(n):
    # number of ways to reach current step is the sum of ways to reach previous step and the step before that (can do 1 or 2 steps)
    prev, curr = curr, prev + curr
  
  # return the number of ways to reach the nth step
  return curr 