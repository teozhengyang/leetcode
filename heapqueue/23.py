# https://leetcode.com/problems/merge-k-sorted-lists/

import heapq
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # initialise heap
        heap = []
        heapq.heapify(heap)
        # initialise result list
        result = ListNode(0)
        curr = result
        
        # push first element of each list into heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        while heap:
            # add smallest element to result list
            val, pos = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            # push next element from the same list into heap
            if lists[pos]:
                heapq.heappush(heap, (lists[pos].val, pos))
                lists[pos] = lists[pos].next
        
        return result.next
