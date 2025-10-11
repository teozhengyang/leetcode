# https://leetcode.com/problems/daily-temperatures/

from typing import List
from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = deque()

        for i in range(len(temperatures)):
            # track current temperature
            curr_temp = temperatures[i]
            # pop from stack and update previous indices until stack is empty or current temperature is not warmer
            while stack and temperatures[stack[-1]] < curr_temp:
                old_temp_index = stack.pop()
                # update days to wait for a warmer temperature
                answer[old_temp_index] = i - old_temp_index
            # add current index to stack
            stack.append(i)
        
        return answer
    