import collections
def solution(begin, target, words):
    
    if target not in words:
        return 0

    # 그래프 생성
    words.append(begin)  # 시작 단어는 words에 없어서 graph 생성 시 포함되지 않았다. 이 코드를 통해 graph 생성과정에 포함시켜야 한다.
    graph = collections.defaultdict(list)
    
    for key in words:
        for value in words:
            
            if key == value:
                continue
            
            diff_count = 0
            for i in range(len(key)):
                if diff_count > 1:
                    break
                    
                if key[i] != value[i]:
                    diff_count += 1
            
            if diff_count == 1:
                graph[key].append(value)
    

    # bfs
    q = collections.deque()
    visited = set()
    
    # queue 세팅 및 방문처리
    q.append((begin, 0))   #(word, count)
    visited.add(begin)
    
    while q:
        w, count = q.popleft()

        if w == target:
            return count
        
        for next_w in graph[w]:

            # 방문했다면 통과
            if next_w in visited:
                continue
            
            # 대기열에 push 하면서 방문처리 까지 같이 진행
            q.append((next_w, count + 1))
            visited.add(next_w)
    
    return 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))