from typing import List

# loop through the list and use a dictionary to store the indices of the numbers
# if the complement of the current number (target - num) is already in the dictionary,
# return the indices of the current number and its complement
# Topics: Arrays, Hash Table
def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in visited:
                return visited[complement], i
            else:
                visited[num] = i
              