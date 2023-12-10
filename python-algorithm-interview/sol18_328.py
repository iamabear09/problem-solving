# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        odd_root = odd_head = head
        even_root = even_head = head.next

        while even_head and even_head.next:
            
            odd_head.next = odd_head.next.next
            even_head.next = even_head.next.next

            odd_head = odd_head.next
            even_head = even_head.next

        odd_head.next = even_root
        return odd_root