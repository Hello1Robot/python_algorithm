from collections import deque

def bfs(start):
    bfs_list = [start]
    
    que = deque()
    que.append(start)

    while que:
        x = que.popleft()
        print(x, end=' ')

        for y in range(len(graph[start])):
            if graph[x][y] == 1 and (y not in bfs_list):
                bfs_list.append(y)
                que.append(y)

def dfs(start, dfs_list=[]):
    dfs_list.append(start)
    print(start, end=' ')

    for y in range(len(graph[start])):
        if graph[start][y] == 1 and (y not in dfs_list):
            dfs(y, dfs_list)

N, M, V = map(int, input().split())

graph = [[0] * (N+1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(V)
print()
bfs(V)