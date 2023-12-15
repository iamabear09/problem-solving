from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []
        #path를 통해 결국 "방문처리"의 역할을 한다고 생각
        path = []
        
        #start를 통해 "탐색할 위치"를 지정 한다고 생각할 수 있다.
        def dfs(start, end, count):
            
            if count == k:
                result.append(path[:])
                return

            for num in range(start, end + 1):
                path.append(num)
                dfs(num + 1, end, count + 1)
                path.pop()
        
        dfs(1, n, 0)
        return result
