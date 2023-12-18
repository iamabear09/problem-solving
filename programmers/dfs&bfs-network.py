import collections


def solution(n, computers):
    
    
    #graph 생성
    graph = collections.defaultdict(list)
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                graph[i].append(j)
    
    #방문처리 array 생성
    visited = [False for _ in range(n)]
    

    count = 0
    

    def dfs(n):

        ## stack에서 pop 이후 예외 처리
        if visited[n]:
            return
        
        ## stack에서 pop 이후 방문처리
        visited[n] = True
        
        ## 다음 탐색 위치 지정하면서 dfs 호출
        for next in graph[n]:
            dfs(next)

    ## 연결된 노드 모두 방문
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i)
            
    return count