# https://leetcode.com/problems/find-k-pairs-with-smallest-sums/

from typing import List
import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Edge cases
        if not nums1 or not nums2 or k == 0:
            return []

        heap = []
        result = []

        # Initialise the heap with the smallest pairs (all elements from nums1 and first element from nums2)
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        while heap and k > 0:
            # update the result with the smallest pair
            _, i, j = heapq.heappop(heap)
            result.append((nums1[i], nums2[j]))
            k -= 1
            
            # If there's a next element in nums2, push the new pair into the heap
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

        return result
            