from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
        "6":"mno", "7":"pqrs", "8":"tuv", "9": "wxyz"}


        #경로 정보가 저장 되어야 한다.
        #여기서는 경로정보가 방문 처리와 비슷한 역할을 한것 같다.
        # 또한 dfs에 당연히 "어디를" 탐색하는지에 대한 정보가 들어가야한다. 따라서 index를 생각할 수 있다.
        def dfs(index, path):

            if len(path) == len(digits):
                result.append(path)
                return

            for c in dic[digits[index]]:
                dfs(index + 1, path + c)
        
        if not digits:
            return []
        
        result = []
        dfs(0, "")
        return result