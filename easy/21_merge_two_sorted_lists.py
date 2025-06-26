from typing import Optional

class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
  # create result list & pointer 
  result = ListNode()
  curr = result
  
  # loop through both list
  while list1 and list2:
    # add node from list1 if smaller value
    if list1.val < list2.val:
      curr.next = list1
      list1 = list1.next
    # add node from list2 if smaller value
    else:
      curr.next = list2
      list2 = list2.next
    # move result pointer
    curr = curr.next
  
  # add remaining nodes from list1 or list2 if not added
  curr.next = list1 if list1 else list2
  
  return result.next
  