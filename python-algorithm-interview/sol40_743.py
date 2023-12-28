import collections
import heapq
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        # 그래프 생성
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        
        # 가중치가 정렬의 기준이 되어야 한다.
        q = [(0, k)]
        dist = collections.defaultdict(int)

        # 힙을 사용하면, 여러 노드를 거치더라도 제일 짧은 거리가 먼저 pop되게 되어있다.
        while q:
            time, node = heapq.heappop(q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(q, (alt, v))
        
        if len(dist) == n:
            return max(dist.values())
        
        return -1 