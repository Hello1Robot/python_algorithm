from collections import deque

def bfs(start,end):
    que = deque()
    que.append(start)
    visited[start] = 1
    while que:
        x = que.popleft()
        if x == end:
            print(visited[x]-1)
            return
        if x-1 >= 0 and not visited[x-1]:
            visited[x-1] = visited[x]+1
            que.append(x-1)
        if x+1 <= 100000 and not visited[x+1]:
            visited[x+1] = visited[x]+1
            que.append(x+1)
        if x*2 <= 100000 and not visited[2*x]:
            visited[2*x] = visited[x]+1
            que.append(2*x)
    

N, K = map(int,input().split())
visited = [0]*200001

bfs(N,K)