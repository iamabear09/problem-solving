from typing import Optional
import collections

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True

        deque = collections.deque()
        node = head
        while node:
           deque.append(node.val)
           node = node.next
        
        while len(deque) > 1:
            if deque.popleft() != deque.pop():
                return False
        
        return True
            