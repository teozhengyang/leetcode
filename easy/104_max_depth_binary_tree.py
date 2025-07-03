from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      if root is None:
          return 0
      # recurse and find the max depth of left and right subtrees
      # and add 1 for the current node
      return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))