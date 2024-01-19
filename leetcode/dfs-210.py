import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # making graph
        graph = collections.defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        result = []
        visited = []
        traced = set()

        def dfs(course):
            # 이미 한번 확인한 Graph라면 True
            if course in visited:
                return True

            # 예외 처리
            if course in traced:
                return False

            # 방문 처리
            visited.append(course)
            traced.add(course)
            for next_crs in graph[course]:
                if not dfs(next_crs):
                    return False
                
            traced.remove(course)
            
            # 먼저 들어야 하는 course 저장
            result.append(course)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return result


## ------------- 정답 -------------

import collections
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        # making graph
        graph = collections.defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        result = []
        visited = []
        traced = set()

        def dfs(course):

            # 정답: 예외처리가 먼저 와야 한다.
            # 예외 처리
            if course in traced:
                return False
            
            # 이미 한번 확인한 Graph라면 True
            if course in visited:
                return True

            # 방문 처리
            visited.append(course)
            traced.add(course)
            for next_crs in graph[course]:
                if not dfs(next_crs):
                    return False
                
            traced.remove(course)
            
            # 먼저 들어야 하는 course 저장
            result.append(course)

            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return result
