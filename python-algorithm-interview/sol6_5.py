'''
올바른 솔루션
나는 "ab"가 입력인 경우의 엣지 케이스를 제대로 처리하지 못했다.
생각도 못했었다.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1: right]
        
        if len(s) < 2 or s == s[::-1]:
            return s
        
        result = ""
        for i in range(len(s) - 1):
            result = max(result,
                         expand(i, i+1),
                         expand(i, i+2),
                         key=len)
            
        return result