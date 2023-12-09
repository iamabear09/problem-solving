
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 그냥 head 변수 사용해도 된다.
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = prev = ListNode()
        root.next = head
        cur_node = head
        

        while cur_node and cur_node.next:

            next_node = cur_node.next
            prev.next = next_node

            #swap
            cur_node.next, next_node.next = next_node.next, cur_node
            
            cur_node, prev = cur_node.next, cur_node
        
        return root.next