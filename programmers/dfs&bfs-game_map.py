import collections
import sys
import copy


# 내 코드 :: 오류 존재한다.
def solution(maps):

    def dfs(row, col, visited, count):
        # 예외처리
        if row < 0 or row >= len(maps) or\
        col < 0 or col >= len(maps[0]) or\
        visited[row][col] == 0:
            return sys.maxsize
        
        # 원하는 상황
        if row == len(maps) - 1 and\
        col == len(maps[0]) - 1:
            return count
        
        # 방문처리
        visited[row][col] = 0
        
        ## !!! 문제점 !!! :: visited는 2차원 배열이다. visited[:] → shallow copy가 발생하므로 올바른 역할 수행 불가능
        return min(dfs(row - 1, col, visited[:], count + 1), #위
                    dfs(row + 1, col, visited[:], count + 1), #아래
                    dfs(row, col - 1, visited[:], count + 1), #왼쪽
                    dfs(row, col + 1, visited[:], count + 1) #오른쪽
                   )
        
        
    count = dfs(0, 0, maps[:], 1)
    if count == sys.maxsize:
        return -1
    
    return count



# 수정한 코드
def solution(maps):

    def dfs(row, col, visited, count):

        # 원하는 상황
        if row == len(maps) - 1 and\
        col == len(maps[0]) - 1:
            return count
        
        # 방문처리
        visited[row][col] = 0

        # 상, 하, 좌, 우
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        
        result = sys.maxsize
        for i in range(4):
            next_r = row + dr[i]
            next_c = col + dc[i]

            # stack에 push할 때, 예외처리 진행
            if next_r < 0 or next_r >= len(maps) or\
                next_c < 0 or next_c >= len(maps[0]) or\
                visited[next_r][next_c] == 0:
                continue

            result = min(result, dfs(next_r, next_c, visited, count + 1))

        # 원상 복귀 → memory를 많이 사용하지 않아도 된다.
        visited[row][col] = 1

        return result
    
    # 여기서 deep copy를 해주어야 한다.    
    result = dfs(0, 0, copy.deepcopy(maps), 1)
    return result if result != sys.maxsize else -1

# BFS
# BFS
def solution(maps):

    #deep copy
    visited = [row[:] for row in maps[:]]

    q = collections.deque()

    #방문처리 하면서 queue에 넣는다.
    q.append((0, 0, 1)) #(row, col, count)
    visited[0][0] = 0

    while q:
        row, col, count = q.popleft()

        if row == len(maps) - 1 and col == len(maps[0]) - 1:
            return count

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        for i in range(4):
            next_r = row + dr[i]
            next_c = col + dc[i]
            
            ## 갈 수 없는 자리는 가지 않는다.
            if next_r < 0 or next_r >= len(maps) or\
            next_c < 0 or next_c >= len(maps[0]) or\
            visited[next_r][next_c] == 0:
                continue

            #방문처리 하면서 queue에 넣는다.
            q.append((next_r, next_c, count + 1))
            visited[next_r][next_c] = 0
    
    return -1