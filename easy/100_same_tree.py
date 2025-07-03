from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
      # Check if both nodes are the same
      if p == q:
          return True
      # If one is None and the other is not, they are not the same
      if p is None or q is None:
          return False
      # check subtrees recursively
      return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)