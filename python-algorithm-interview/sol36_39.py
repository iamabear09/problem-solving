from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result = []
        path = []
        def backtracking(sum, idx):

            if sum > target:
                return
            
            if sum == target:
                result.append(path[:])
                return

            for i in range(idx, len(candidates)):
                num = candidates[i]
                
                path.append(num)
                backtracking(sum + num, i)
                path.pop()
        
        backtracking(0, 0)
        return result

