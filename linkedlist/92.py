# https://leetcode.com/problems/reverse-linked-list-ii/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# refer to 92.py.jpeg for visualisation
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        result = ListNode(0)
        result.next = head
        prev = result
        
        for _ in range(left - 1):
            prev = prev.next

        curr = prev.next

        for _ in range(left, right):
            # save next node
            next_node = curr.next
            # next of curr = next of next node
            curr.next = next_node.next
            # next of next node = curr
            next_node.next = prev.next
            # next of prev = next
            prev.next = next_node
        
        return result.next