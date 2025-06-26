from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    # create a dictionary to store visited numbers and their indices
    visited = {}
    # iterate through the list of numbers
    for i, num in enumerate(nums):
        complement = target - num
        # if the complement is found in visited, return the indices
        if complement in visited:
            return visited[complement], i
        # if the complement is not found, add the number and its index to visited
        else: 
            visited[num] = i
              