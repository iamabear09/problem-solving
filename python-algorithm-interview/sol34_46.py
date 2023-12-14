from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        path = []
        result = []

        def dfs():
            if len(path) == len(nums):
                result.append(path[:])
                return
            for n in nums:
                if n in path:
                    continue
                path.append(n)
                dfs()
                path.remove(n)
        dfs()
        return result


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, used): 
            if len(path) == len(nums): 
                result.append(path[:]) 
                return 
            
            #이렇게 따로 배열을 만들어서 건너 뛰게 할 수 있다. => 이렇게 하면 list를 새로 만들지 않아도 된다.
            for i in range(len(nums)): 
                if not used[i]: 
                    path.append(nums[i]) 
                    used[i] = True 
                    dfs(path, used) 
                    path.pop() 
                    used[i] = False 
        result = [] 
        dfs([], [False] * len(nums)) 
        return result 
