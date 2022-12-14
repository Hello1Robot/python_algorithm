from collections import deque

def bfs(start,end):
    que = deque()
    que.append(start)
    visited[start] = 0
    res_cnt = -1
    cnt = 0
    flag = 0
    while que:
        x = que.popleft()
        if x == end and not flag :
            print(visited[x])
            res_cnt = visited[x]
            cnt += 1
        elif x == end and flag and visited[x] == res_cnt:
            cnt += 1
            visited[x] = 0
            
        if x-1 >= 0 and visited[x-1] > visited[x]+1:
            visited[x-1] = visited[x]+1
            que.append(x-1)
        if x+1 <= 100000 and visited[x+1] > visited[x]+1:
            visited[x+1] = visited[x]+1
            que.append(x+1)
        if x*2 <= 100000 and visited[2*x] > visited[x]+1:
            visited[2*x] = visited[x]+1
            que.append(2*x)

    print(cnt)
    

N, K = map(int,input().split())
visited = [1e9]*200001

bfs(N,K)