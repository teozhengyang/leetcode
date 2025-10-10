# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        curr = result

        while head:
            # duplicate value detected
            if head.next and head.val == head.next.val:
                curr_value = head.val
                # advance through all duplicate
                while head and head.val == curr_value:
                    head = head.next
            # unique value
            else:
                curr.next = head
                curr = curr.next
                head = head.next
        
        curr.next = None
        return result.next