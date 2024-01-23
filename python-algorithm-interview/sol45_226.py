# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):

            if node is None:
                return
            
            dfs(node.left)
            dfs(node.right)

            node.left, node.right = node.right, node.left

            return 

        dfs(root)
        return root
    

    

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        
        return None