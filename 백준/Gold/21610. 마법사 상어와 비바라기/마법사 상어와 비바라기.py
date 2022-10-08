# 모든 구름이 di 방향으로 si칸 이동한다.
# 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
# 구름이 모두 사라진다.
# 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면, 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c)에 있는 바구니의 물이 양이 증가한다.
# 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
# 예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고, (N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
# 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(N)]

dx = [0,0,-1,-1,-1,0,1,1,1]
dy = [0,-1,-1,0,1,1,1,0,-1]
que = deque()
que2 = deque()
que.append((N-1, 0))
que.append((N-1, 1))
que.append((N-2, 0))
que.append((N-2, 1))
for _ in range(M):
    i, r = map(int,input().split())
    visited = [[0]*N for _ in range(N)]
    while que:
        x, y = que.popleft()
        nx = (x + dx[i]*r) % N
        ny = (y + dy[i]*r) % N
        field[nx][ny] += 1
        que2.append((nx,ny))
        visited[nx][ny] = 1
    
    while que2:
        x, y = que2.popleft()
        for xx, yy in ((1,-1), (-1,1), (-1,-1), (1,1)):
            nx = x + xx
            ny = y + yy
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if field[nx][ny]:
                field[x][y] += 1

    for a in range(N):
        for b in range(N):
            if field[a][b] >= 2 and not visited[a][b]:
                field[a][b] -= 2
                que.append((a,b))


tot = 0
for c in range(N):
    for d in range(N):
        tot += field[c][d]

print(tot)