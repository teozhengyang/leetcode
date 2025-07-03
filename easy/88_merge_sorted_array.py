from typing import List

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
  index_1 = m - 1
  index_2 = n - 1
  index_merge = m + n - 1
  
  # merge in reverse order to fill nums1 from the end (end with 0)
  while index_2 >= 0:
    if index_1 >= 0 and nums1[index_1] > nums2[index_2]:
      nums1[index_merge] = nums1[index_1]
      index_1 -= 1
    else:
      nums1[index_merge] = nums2[index_2]
      index_2 -= 1
    index_merge -= 1
  