# https://leetcode.com/problems/insertion-sort-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Insertion sort by creating a new sorted linked list
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)

        while head:
            # find from start of result
            curr = result.next
            prev = result
            # find the right place to insert
            while curr is not None and curr.val < head.val:
                prev = curr
                curr = curr.next
            # insert between prev and curr
            prev.next = ListNode(head.val)
            prev.next.next = curr
            head = head.next
        
        return result.next   

# Alternative solution using array to store values
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result_list = []

        while head:
            result_list.append(head.val)
            head = head.next
        
        result_list.sort()

        result = ListNode(0)
        curr = result

        for num in result_list:
            curr.next = ListNode(num)
            curr = curr.next
        
        return result.next         