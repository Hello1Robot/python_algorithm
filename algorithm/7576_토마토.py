from collections import deque
import sys
input = sys.stdin.readline

# 시간초과
# M과 N 순서로 주어짐. 그냥 그렇게 받고 x축 y축 알아서 쓰면 될 듯
M, N = map(int,input().split())

dx = [0,0,-1,1]
dy = [1,-1,0,0]
# 하나의 줄에는 가로 줄의 정보. 그냥 N개만큼 받으면 필드
field = [list(map(int,input().split())) for _ in range(N)]
# 1은 익은 토마토, 0은 익지 않은 토마토, -1은 토마토가 들어있지 않은 칸
# 모두 익어있는 상황이면 0 출력
# 모두 익지는 못하는 상황이면 -1 출력
que = deque()
for i in range(N):
    for j in range(M):
        if field[i][j] == 1:
            que.append((i,j))
res = 0
cnt = 0
while que:
    x,y = que.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 범위 안이고, field가 0일 때
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if field[nx][ny] == 0:
            field[nx][ny] = field[x][y] + 1
            que.append((nx,ny))



days = 0
for i in range(N):
    for j in range(M):
        if field[i][j] > days:
            days = field[i][j]
        if field[i][j] == 0:
            print(-1)
            exit()
        
print(days-1)
