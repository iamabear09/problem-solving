import collections
import heapq
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        graph = collections.defaultdict(list)
        
        for start, end, cost in flights:
            graph[start].append((end, cost))
        
        q = [(0, src, k)]

        ##기존에 없던 코드 : 답지보고 적음
        css=[(float("infinity"), 0)]*n
        css[src]=(0,k)

        while q:
            cost, node, k = heapq.heappop(q)
            
            #BFS의 방문처리와 비슷한 과정
            if node == dst:
                return cost
            
            #K==0이면, 해당 지점에서 마지막으로 한번 더 진행 할 수 있다.
            if k >= 0:
                for next_node, next_cost in graph[node]:


                    ## 기존에 없던 코드 : 답지보고 적음
                    if css[next_node][0]> cost + next_cost or css[next_node][1] < k - 1:
                        css[next_node]=(cost + next_cost, k - 1)
                        heapq.heappush(q, (cost + next_cost, next_node, k - 1))
        
        return -1

# 기존 내 코드는의 문제는 q에 방문하지 않아도 될 node들이 잔뜩 남아있다는 것이다.
# 전부다 방문해야하는 경우, 쓸데없는 값을 넣지 않도록 주의해야 한다.

import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        grid=[[] for i in range(n)]
        for frm,to,cst in flights:
            grid[frm].append((cst,to))
        
        st=[(0,0,src)]
        heapq.heapify(st)
        css=[(float("infinity"),float("infinity"))]*n
        css[src]=(0,0)
        while st:
            cst,stop,x=heapq.heappop(st)
            if x==dst:
                return cst
            if stop<=k:
                for ct,to in grid[x]:
                    # 이게 왜 필요할까? → 필요없는 값을 넣지 않기 위해서 필요하다.
                    # css[next_node][0]> cost + next_cost :: cost가 이전보다 싸면 일단 다음에 방문할 가치가 있다.
                    # css[next_node][1] < k - 1 :: 또는 방문 기회가 이전보다 많이 남았으면 방문할 가치가 있다.
                    # 생각해보면 마지막 방문보다더 멀리갈 기회도 적고, 값도 비싸면 이 길은 아예 버려야 하는 길이다.
                    # 하지만 나머지는 적어도 도달할 가능성이나, 더 싸게 방문할 가능성을 열어두고 있다.
                    if css[to][0]>ct+cst or css[to][1]>stop+1:
                        css[to]=(ct+cst,stop+1)
                        heapq.heappush(st,(cst+ct,stop+1,to))

        return -1