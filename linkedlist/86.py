# https://leetcode.com/problems/partition-list/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left = ListNode(0)
        curr_left = left
        right = ListNode(0)
        curr_right = right

        # update each list
        while head:
            if head.val < x:
                curr_left.next = ListNode(head.val)
                curr_left = curr_left.next
            elif head.val >= x:
                curr_right.next = ListNode(head.val)
                curr_right = curr_right.next                
            head = head.next
        
        # link all lists together
        curr_left.next = right.next
        
        return left.next