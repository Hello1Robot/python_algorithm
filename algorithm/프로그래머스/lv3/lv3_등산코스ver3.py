# 힙큐를 쓰면서 방문처리를 어떻게 할 지가 관건인듯?
# 방문노드를 힙큐에서 어떻게 처리할까
# 1. str으로 만들어서 in 확인하고 붙이기
# n이 5만이니까 계속 이어서 str만드는것도 메모리터질듯?ㅋ;;
# 그래도 한번 트라이해볼까
import heapq


def solution(n, paths, gates, summits):
    answer = []
    max_intensity = 100000000
    summit_num = 50001
    que = []
    field = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    for a, b, c in paths: # 양방향이니 양쪽에 넣기
        field[a].append((b,c))
        field[b].append((a,c))

    for gate in gates: # 게이트 전부 힙큐에 넣고 돌리기
        visited[gate] = 1
        heapq.heappush(que, (0, gate))
    summits = set(summits)
    while que:
        cost, start = heapq.heappop(que)
        if cost > max_intensity:
            continue
        if start in summits:
            if cost == max_intensity:
                if summit_num > start:
                    summit_num = start
            else:
                max_intensity = cost
                summit_num = start
            continue

        for x, y in field[start]:
            if x in gates:
                continue
            if not visited[x]:
                visited[x] = 1
                heapq.heappush(que, (max(y,cost), x))
    

    
    answer.append(summit_num)
    answer.append(max_intensity)

    return answer



print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1,3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2,3,4] ))