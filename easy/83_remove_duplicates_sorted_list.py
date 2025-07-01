from typing import Optional


class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next
class Solution:
  def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # initialise pointer
    curr = head

    # iterate through the list
    while curr and curr.next:
      # if current value is equal to next value, skip the next node
      if curr.val == curr.next.val:
        curr.next = curr.next.next
      else: # if they are not equal, move to the next node
        curr = curr.next
        
    return head
      
      