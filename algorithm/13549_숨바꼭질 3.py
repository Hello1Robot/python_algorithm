from collections import deque
import heapq

def bfs(start,end):
    que = []
    heapq.heappush(que, start)
    # que.append(start)
    visited[start] = 1
    while que:
        x = heapq.heappop(que)
        # x = que.popleft()
        if x == end:
            print(visited[x]-1)
            return
        if x-1 >= 0 and not visited[x-1]:
            visited[x-1] = visited[x]+1
            heapq.heappush(que, x-1)
        if x+1 <= 100000 and not visited[x+1]:
            visited[x+1] = visited[x]+1
            heapq.heappush(que, x+1)
        if x*2 <= 100000 and (not visited[2*x] or visited[2*x] > visited[x]) :
            visited[2*x] = visited[x]
            heapq.heappush(que, 2*x)
    

N, K = map(int,input().split())
visited = [0]*200001

bfs(N,K)