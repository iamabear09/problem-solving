from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        path = []
        def dfs(idx):
            
            # dfs에서 방문하게 된 위치이다. 따라서 result에 결과 append
            result.append(path[:])

            if idx >= len(nums):
                return
            
            for i in range(idx, len(nums)):
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        dfs(0)
        return result

