from heapq import heapify, heappush

# 문제 아이디어 설명
# 1. 왼쪽 / 오른쪽 에 따라서 동작이 달라진다. → 왼쪽 오른쪽 구분
# 2. 왼쪽의 경우, 현재 x 좌표에서 높이가 가장 높아야 저장할 수 있다. → 가장 높은 높이를 계속 알고 있어야 한다.
# 3. 오른쪽의 경우, 현재 나의 높이보다 한단계 낮은 높이를 알 수 있어야 한다.

# 핵심 :: 우선순위 큐를 언제 사용해야 하는가? 
# 우선순위 큐에서 왼쪽 높이를 넣어놓고, 오른쪽 높이를 만났을 때 오른쪽 높이를 제거함으로서 하나의 선을 그릴 수 있다.
# 우선순위 큐를 통해 높이의 레벨을 계속 알 수 있다.

def solution(buildings):
    buildings.sort()
    
    points = [[(left, -1, height), (right, 1, height)] for left, right, height in buildings]
    
    # 아! 중첩 리스트를 하나의 리스트로 만드는 과정 :: [] + [(1, -1, 4)] + [(8, 1, 4] ... 
    points = sum(points, [])


    points.sort()

    heap = []
    current_height = 0
    heappush(heap, current_height)

    result = []
    for x, d, h in points:
        # 왼쪽 포인트면 높이 저장
        if d < 0:
            heappush(heap, -h)
        
        # 오른쪽 포인트면 높이 제거
        else:
            heap.remove(-h)
            heapify(heap)
        
        # 현재 높이가 가장 높지 않으면,
        if current_height != heap[0]:

            # 결과에 현재 높이 저장
            result.append([x, -heap[0]])
            current_height = heap[0]
    
    return result



# buildings = [[1, 8, 4], [2, 4, 10], [3, 5, 6], [10, 12, 6]]
# print(solution(buildings))