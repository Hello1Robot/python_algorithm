from collections import deque
import heapq

def bfs(start,end):
    que = deque()
    que.append(start)
    # que.append(start)
    visited[start] = 0
    while que:
        x = que.popleft()
        if x == end:
            print(visited[x])
            return
        if x-1 >= 0 and visited[x-1] > visited[x]+1:
            visited[x-1] = visited[x]+1
            que.append(x-1)
        if x+1 <= 100000 and visited[x+1] > visited[x]+1:
            visited[x+1] = visited[x]+1
            que.append(x+1)
        if x*2 <= 100000 and visited[2*x] > visited[x] :
            visited[2*x] = visited[x]
            que.append(2*x)
    

N, K = map(int,input().split())
visited = [1e9]*200001

bfs(N,K)