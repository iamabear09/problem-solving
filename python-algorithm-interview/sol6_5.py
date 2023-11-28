# 비효율 적인 풀이다.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ""
        for idx in range(0, len(s)):
            result = max(self.startTwoWords(s, idx), result, key=len)
            result = max(self.startTreeWords(s, idx), result, key=len)
        
        return result
    
    def startTwoWords(self, s, idx):
        left = idx
        right = idx + 1
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1: right]

    def startTreeWords(self, s, idx):
        left = idx
        right = idx + 2

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        return s[left + 1: right]