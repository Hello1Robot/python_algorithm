from collections import deque

def bfs(x):
    que = deque()
    st = str(x)
    que.append((x,st))
    visited[x] = 0
    while que:
        x, st = que.popleft()
        if x == 1:
            return visited[x], st
        if not x % 3 and visited[x//3] == -1:
            visited[x//3] = visited[x] + 1
            que.append((x//3, st+' '+str(x//3)))
        if not x % 2 and visited[x//2] == -1:
            visited[x//2] = visited[x] + 1
            que.append((x//2, st+' '+str(x//2)))
        if visited[x-1] == -1:
            visited[x-1] = visited[x]+1
            que.append((x-1, st+' '+str(x-1)))
        
    




N = int(input())
visited = [-1]*10000000
cnt, vis = bfs(N)
print(cnt)
print(vis)