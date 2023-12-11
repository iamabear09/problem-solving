# Definition for singly-linked list.

# Reverse List 하는 방법 == 새로운 길을 만든다고 생각하자.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        if not head or left == right:
            return head
        
        root = ListNode()
        root.next = head

        l, r = root, root
        
        for _ in range(left - 1):
            l = l.next
        for _ in range(right + 1):
            r = r.next

        for _ in range(right - left + 1):
            node = l.next
            
            node.next, l.next = r, node.next
            r = node
        l.next = r
        
        return root.next


        
