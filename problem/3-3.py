def solution(delay, N):

    return 1 + recursive(1, 0, delay, N) + recursive(1, delay, delay, N)

def recursive(time, left_time, delay, N):

    if time == N:
        return 1
    
    if left_time != 0:
        return recursive(time + 1, left_time - 1, delay, N)


    return 1 + recursive(time + 1, 0, delay, N) + recursive(time + 1, delay, delay, N)



## solution
def solution(delay, N):
    q = []
    q.append(0)

    count = 1
    # 아! 각 단계를 queue 2개를 통해 나타냈다. 좀더 직관적인 풀이 방법인것 같다.
    for _ in range(N):
        new_q = []
        while q:
            d = q.pop(0)
            if d == 0:
                new_q.append(0)
                new_q.append(delay)
                count += 2
            else:
                new_q.append(d - 1)
        q = new_q
    
    return count
    
