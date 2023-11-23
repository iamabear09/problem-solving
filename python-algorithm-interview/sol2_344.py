from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        if len(s) <= 1:
            return

        l = 0
        r = len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return 
    


class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        return 