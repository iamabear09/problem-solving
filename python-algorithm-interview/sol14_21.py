
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        
        if not list1:
            return list2
         
        if list1.val > list2.val:
            list1, list2 = list2, list1
        
        list1.next = self.mergeTwoLists(list1.next, list2) 

        return list1
    
# 문제를 작게 나눠서 푸는 방법 → 전형적인 재귀함수적인 생각 