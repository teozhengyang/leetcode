from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
      # Helper function to check if two trees are symmetric
      def check_sym(left, right):
          if not left and not right:
              return True
          if not left or not right:
              return False
          return (left.val == right.val and check_sym(left.left, right.right) and check_sym(left.right, right.left)) # mirror image check
      return check_sym(root.left, root.right)