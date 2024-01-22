# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    result = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def get_length(node, val):

            # 예외처리
            if node is None:
                return 0

            # 현재 트리에서 가장 긴 길이 계산
            left = get_length(node.left, node.val)
            right = get_length(node.right, node.val)

            self.result = max(self.result, left + right)

            # 위 node로 값 전달
            return max(left, right) + 1 if node.val == val else 0

        # 예외 처리 잊어버렸다.
        if root is None:
            return 0
            
        get_length(root, root.val)
        return self.result
    

## 책 솔루션
class Solution:
    result = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def get_length(node):

            # 예외처리
            if node is None:
                return 0

            # 현재 트리에서 가장 긴 길이 계산
            left = get_length(node.left)
            right = get_length(node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
                

            self.result = max(self.result, left + right)

            # 위 node로 값 전달
            return max(left, right)

        get_length(root)
        return self.result