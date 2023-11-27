from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        # defaultdict 초기값 [] ❌
        # [] >> list

        for word in strs:
            result[''.join(sorted(word))].append(word)
        
        return list(result.values())