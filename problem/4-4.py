import heapq
from queue import PriorityQueue

def solution(start, time):
    tasks = [[start[i], time[i], i] for i in range(len(start))]
    tasks.sort(key=lambda x: (x[0], x[2]))

    heap = []
    idx = 0
    cur_time = 0
    result = [0 for _ in range(len(tasks))]

    for (t, s, idx) in tasks:

        while heap:
            (t_, s_, i_) = heapq.heappop(heap)
            cur_time += t_
            result[idx] = i_

        if cur_time > s:
            heapq.heappush(heap, (t, s, idx))
            continue

        if cur_time < s:
            cur_time = s
            heapq.heappush(heap, (t, s, idx))

        if not heap and t >= cur_time:
            heapq.heappush(heap,)
    
    while heap:
        (t_, s_, i_) = heapq.heappop(heap)
        cur_time += t_
        result[idx] = i_



### 솔루션

def solution(start, time):
    tasks = [(st[0], st[1], i)
            for i, st in enumerate(zip(start, time))]
    
    tasks.sort(key=lambda x: (x[0], x[2]))
    
    pq = PriorityQueue()
    answer = [0 for _ in range(len(tasks))]
    idx = 0
    time = 0

    # while문 구성이 어려웠다. :: 큰 틀에서 문제가 끝나는 시점을 파악해야했다.
    # idx 가 마지막 까지
    while idx < len(answer):

        # 작업 채워 넣기
        while tasks and time >= tasks[0][0]:
            start_, time_, idx_ = tasks[0]
            pq.put((time_, idx_, start_))
            del tasks[0]

        # 작업이 있으면 작업 수행 :: 나는 여기를 while문으로 하려고 했다.
        if not pq.empty():
            current_task = pq.get()
            time += current_task[0]
            answer[idx] = current_task[1]
            idx += 1

        # 작업도 없고 시간도 아직 작으면 작업 채워 넣기
        else:
            # 현재 시간을 작업 시작 시간으로 만든다.
            time = tasks[0][0]
            
            # time = tasks[0][0] 하면 무조건 time == tasks[0][0] 은 True인데?
            while tasks and time >= tasks[0][0]:
                start_, time_, idx_ = tasks[0]
                pq.put((time_, idx_, start_))
                del tasks[0]
    return answer