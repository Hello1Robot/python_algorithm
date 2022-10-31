# 다익스트라 문제인 줄 알았는데, 조금 접근이 다름
# 경로의 길이와 상관없이, '한번에 다른 노드로 넘어가는 비용이 가장 적은 코스'
# 양방향이라서 돌아오는 건 고려안해도 됨
# max비용이 가장 낮은 길 찾기
# 백트래킹도 될듯? 
# 스타트 노드들만 반복으로 해서 DFS인가 뭔가 돌리고
# 만약 도달한 지점이 봉우리 지점이면, 해당 지점까지의 max_int 비교
# 길을 선택하면서 int가 이전 intensity보다 높으면 애초에 탐색안하기
# 만약 intensity가 같을 경우에는 봉우리넘버가 낮은 걸 선택
# BFS로 하면 visited 처리가 좀 까다로워서
# 다른 방법을 탐색해야 할듯

max_intensity = 100000000
summit_num = 50001

def 경로찾기(start, max_cost, field, visited, summits):
    global max_intensity
    global summit_num

    if max_cost > max_intensity: # 백트래킹
        return
    if start in summits:
        if max_cost == max_intensity:
            if summit_num > start:
                start = summit_num
        elif max_cost < max_intensity:
            max_intensity = max_cost
            summit_num = start
        return
    for x, y in field[start]:
        if not visited[x]:
            visited[x] = 1
            경로찾기(x, max(max_cost, y), field, visited, summits)
            visited[x] = 0



def solution(n, paths, gates, summits):
    answer = []
    global max_intensity
    global summit_num
    field = [[] for _ in range(n+1)]
    for a, b, c in paths: # 양방향이니 양쪽에 넣기
        field[a].append((b,c))
        field[b].append((a,c))


    for gate in gates:
        visited = [0]*(n+1)
        visited[gate] = 1
        경로찾기(gate, 0, field, visited, summits)
    
    answer.append(summit_num)
    answer.append(max_intensity)
    max_intensity = 100000000
    summit_num = 50001
    return answer



print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1,3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2,3,4] ))