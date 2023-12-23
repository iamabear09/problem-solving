import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        visited = [False] * numCourses
        visited_node = [False] * numCourses

        # 그래프 생성
        graph = collections.defaultdict(list)
        for a,b in prerequisites:
            graph[a].append(b)

        
        def dfs(course):

            if visited[course]:
                return False
            
            if visited_node[course]:
                return True

            visited[course] = True

            # 여기서도 조건을 판별했어야 한다.
            for next in graph[course]:
                if not dfs(next):
                    return False
                
            # 형제 노드 방문 때문에 순환노드로 착각할 수 있다.
            visited[course] = False

            visited_node[course] = True


            # 조건 처리
            return True
        
        for node in list(graph):
            if not dfs(node):
                return False
            
        return True
