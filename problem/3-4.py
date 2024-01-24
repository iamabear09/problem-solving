
# 생각해보면 이것 또한 Graph를 탐새하는 문제이다.
# 그러면 Graph 탐색과 비슷하게 문제를 해결할 수 있다는 생각을 배울 수 있다.
def solution(x1, y1, x2, y2):

    # 시작점
    set_a = {(x1, y1)}
    # 방문한 자리 :: 방문한 곳은 다시 방문하지 않도록 한다.
    hist_a = set_a.copy()
    # 시작점 
    set_b = {(x2, y2)}
    # 방문한 자리
    hist_b = set_b.copy()


    if (x1, y1) == (x2, y2):
        return 0
    
    time = 1
    while True:

        # 다음 방문 할 자리
        new_set_a = set()
        new_set_b = set()

        for pos_a in set_a:
            new_set_a.add((pos_a[0] + 1, pos_a[1]))
            new_set_a.add((pos_a[0], pos_a[1] + 1))
            new_set_a.add((pos_a[0] - 1, pos_a[1]))
            new_set_a.add((pos_a[0], pos_a[1] - 1))
        
        for pos_b in set_b:
            new_set_b.add((pos_b[0] + 1, pos_b[1] + 1))
            new_set_b.add((pos_b[0] - 1, pos_b[1] + 1))
            new_set_b.add((pos_b[0] + 1, pos_b[1] - 1))
            new_set_b.add((pos_b[0] - 1, pos_b[1] - 1))
        
        # 방문할 자리 계산
        new_set_a = new_set_a - hist_a
        new_set_b = new_set_b - hist_b

        for pos_a in new_set_a:
            if pos_a in new_set_b:
                return time

        set_a = new_set_a
        set_b = new_set_b

        # 방문 처리
        hist_a = hist_a.union(set_a)
        hist_b = hist_b.union(set_b)

        time += 1