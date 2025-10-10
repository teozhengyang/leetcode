# https://leetcode.com/problems/add-two-numbers/

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        result = ListNode(0)
        curr = result

        while l1 or l2 or carry:
            # add l1 to carry
            if l1:
                carry += l1.val
                l1 = l1.next
            # add l2 to carry
            if l2:
                carry += l2.val
                l2 = l2.next
            # creat next node
            curr.next = ListNode(carry % 10)
            curr = curr.next
            # update carry
            carry = 1 if carry > 9 else 0

        return result.next
        