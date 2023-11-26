import re
from typing import *
import collections

# r의미 → raw string으로 처리 하겠다. 
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                    if word not in banned]

        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]

# max에 dict 전달하면, 기본적으로 key값이 가장 큰 것이 출력되는 것 같다. 
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                    if word not in banned]

        counts = collections.defaultdict(int)
        for w in words:
            counts[w] += 1

        return max(counts, key=counts.get)
