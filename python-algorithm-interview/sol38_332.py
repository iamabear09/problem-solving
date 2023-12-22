import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        # 그래프를 만들어야 한다.
        graph = collections.defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]].append(ticket[1])

        # 한 지점에서 여러 갈래길이 나오면, 어떤 순서로 방문할지 설정
        for key in graph:
            graph[key].sort(reverse=True)
        
        itinerary = []

        def dfs(cur):
            # 일반적인 DFS의 경우, 이 자리에 예외처리 로직이 존재한다.

            # 일반적인 DFS의 경우, 이 자리에 핵심 로직이 들어간다.
            # ex) 원하는 조건이 맞으면, 어떤 Action 수행

            # 일단 다 방문하면서
            while graph[cur]:
                dfs(graph[cur].pop())
            
            # While문 통과 → 막다른 길이다.
            # 막다른 길에 들어가면, 이 때 핵심로직 처리
            itinerary.append(cur)
        
        dfs("JFK")

        return reversed(itinerary)