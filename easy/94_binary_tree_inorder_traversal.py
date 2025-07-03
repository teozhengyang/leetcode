from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Recursive inorder traversal
        ans = []
        def inorder(node, ans):
            if node is None:
                return None
            inorder(node.left, ans)
            ans.append(node.val)
            inorder(node.right, ans)
        inorder(root, ans)
        return ans
      
        # Iterative inorder traversal using stack
        ans = []
        stack = []
        if root is None:
            return None
        while True: 
            while root: 
                # Push all left nodes onto the stack
                stack.append(root)
                root = root.left
            # If stack is empty, we are done
            if not stack:
              return ans
            # Pop from stack and visit the node
            curr = stack.pop()
            # Add the current node's value to the result
            ans.append(curr.val)
            # Traverse to right subtree
            root = curr.right
        return ans