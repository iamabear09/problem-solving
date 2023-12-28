def solution(N):

    dp = [0] * (N + 1)

    #dp 테이블 초기화
    dp[1], dp[2] = 1, 2

    #dp 순회
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]
    
    print(dp[N])