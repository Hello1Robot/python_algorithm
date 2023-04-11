from sys import stdin, setrecursionlimit; input = stdin.readline
setrecursionlimit(10000000)

def DFS(x):
    global cnt
    visited[x] = cnt
    field[x].sort(reverse=True)
    for i in field[x]:
        if not visited[i]:
            cnt += 1
            DFS(i)

N, M, S = map(int,input().split())

field = [[] for _ in range(N+1)]
visited = [0]*(N+1)
cnt = 1
for _ in range(M):
    a, b = map(int,input().split())
    field[a].append(b)
    field[b].append(a)

DFS(S)

for ans in visited[1:]:
    print(ans)

