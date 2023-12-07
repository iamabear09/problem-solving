# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        node, prev = head, None
        while node:
            next, node.next = node.next, prev
            prev, node = node, next
        
        return prev
    
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverse(node, prev):
            if not node:
                return prev
            
            next, node.next = node.next, prev
            return reverse(next, node)
        
        return reverse(head, None)