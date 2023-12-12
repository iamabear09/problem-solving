from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        result = 0

        # 상, 하, 좌, 우
        dr = [0,0,-1,1]
        dc = [-1,1,0,0]

        def dfs(r, c):

            #여기서 예외처리도 가능 하다. 즉, Stack에서 Pop 한 후에 예외처리 가능하다.
            if (grid[r][c] == "0"):
                return
            
            # Stack에서 pop 한 후 방문 처리 가능 >> 하지만, BFS에서는 Queue에 Push 직후 방문처리를 했다.
            grid[r][c] = "0"
            
            for i in range(4):
                next_r = r + dr[i]
                next_c = c + dc[i]
                
                # 여기서 예외처리 가능하다. >> 즉, stack에 넣기 전에 예외 처리 가능 :: 재귀 호출 전에 예외 처리 가능
                if next_r < 0 or next_r >= len(grid) or next_c < 0 or next_c >= len(grid[0]):
                    continue
                dfs(next_r, next_c)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r,c)
                    result += 1
        return result
    

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        stack = []
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    stack.append((i, j))

                    while stack:
                        r, c = stack.pop()
                        print(r)
                        print(c)

                        if r < 0 or r >= len(grid) or \
                            c < 0 or c >= len(grid[0]) or \
                            grid[r][c] == "0":
                            continue #return

                        grid[r][c] = "0"

                        stack.append((r - 1, c))
                        stack.append((r + 1, c))
                        stack.append((r, c - 1))
                        stack.append((r, c + 1))
        return count