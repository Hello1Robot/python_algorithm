from sys import stdin; input=stdin.readline

def LIS(rst):
    global res
    DP = [1] * (ms+1)
    for i in range(1,ms+1):
        for j in range(0,i):
            if rst[i] > rst[j]:
                DP[i] = max(DP[j]+1, DP[i])
    x = max(DP)
    if x > res:
        res = x
    return


def DFS(x, y, cnt):
    if cnt > (N-1)*2:
        return
    if x == N-1 and y == N-1:
        LIS(route)
    # 백트래킹 요소 하나 만들기
    
    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx = x + dx
        ny = y + dy
        
        if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny] == 1:
            continue

        visited[nx][ny] = 1
        route.append(field[nx][ny])
        DFS(x, y, cnt+1)
        route.pop()
        visited[nx][ny] = 0


N = int(input())
field = [tuple(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
route = [field[0][0]]
ms = ((N-1)*2)+1
res = 0
DFS(0, 0, 0)
print(res)

