def solution(numbers, target):

    def dfs(cur_idx, sum):

        ## 방문처리와 비슷한 과정
        ## stack에서 pop 했을 때, 방문 처리를 진행한다.
        if cur_idx == len(numbers) and sum == target:
            return 1
        
        ## 예외처리 과정
        ## stack에서 pop 한 이후 예외처리 진행한다.
        if cur_idx >= len(numbers):
            return 0
        
        ## 다음 진행 값 결정
        minor_sum = sum - numbers[cur_idx]
        plus_sum = sum + numbers[cur_idx]

        ##재귀호출 후 결과를 더해서 상위로 올리는 방법
        count = dfs(cur_idx + 1, minor_sum) + dfs(cur_idx + 1, plus_sum)
        
        return count
    
    return dfs(0, 0)
