# Definition for a binary tree node.

import collections
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        def depthCheck(node, depth):
            
            if not node:
                return 0
            
            return depth + 1 + max( depthCheck(node.left, depth), depthCheck(node.right, depth) )

        
        return depthCheck(root, 0)
    

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        if root is None:
            return 0
        
        queue = collections.deque([root])
        depth = 0

        # BFS의 반복횟수를 확인하는 방법이다.
        while queue:
            depth += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return depth
