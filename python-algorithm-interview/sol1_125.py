import collections

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
    
        while len(str) > 1:
            if strs.pop(0) != strs.pop():
                return False
        
        return True
            

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
    
        while len(str) > 1:
            if strs.pop(0) != strs.pop():
                return False
        
        return True



class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
    
        while len(str) > 1:
            if strs.popleft() != strs.pop():
                return False
        
        return True
            