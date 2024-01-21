# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class Solution:
    result = 0
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):

            if node is None:
                return 0
            
            left_len = dfs(node.left)
            right_len = dfs(node.right)
            
            self.result = max(self.result, left_len + right_len)
            
            return 1 + max(left_len, right_len)
        
        dfs(root)
        return self.result
            
