def solution(n):
    if n < 2:
        return 0
    
    result = [1 for _ in range(n)]
    result[0], result[1] = 0, 0
    
    for i in range(2, n):
        if result[i] == 1:
            num = i * 2
            while num < n:
                result[num] = 0
                num += i

    return sum(result)

# 결국 전부다 순회를 하긴 해야한다. 하지만, 매번 같은 계산을 반복하기에는 너무 힘들다.
# 따라서 "배열에 결과를 기록" 후 "배열 값으로 갯수 계산"