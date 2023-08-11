# 구슬 탈출 2와 비슷
# 횟수 제한이 없음 -> 반복되는 경우, 제외해야 함
# visited 만들어서 저장하여 판별하기
from collections import deque

N, M = map(int,input().split())

field = [list(input()) for _ in range(N)]
red_x, red_y, blue_x, blue_y, end_x, end_y = -1, -1, -1, -1, -1, -1

# 상 하 좌 우 - 0, 1, 2, 3
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if field[i][j] == "R":
            red_x = i
            red_y = j
        if field[i][j] == "B":
            blue_x = i
            blue_y = j
        if field[i][j] == "O":
            end_x = i
            end_y = j
que = deque()
res = -1
visited = []
for i in range(4):
    que.append((red_x, red_y, blue_x, blue_y, i, 0)) # 처음에는 네 방향 모두 탐색
    visited.append((red_x, red_y, blue_x, blue_y))

while que:
    rx, ry, bx, by, d, cnt = que.popleft()


    if rx == end_x and ry == end_y: # 빨간 게 도착했으면
        res = cnt
        break
    
    nrx, nry = rx, ry
    while True: # 벽이나 구멍일 때 까지 움직이기
        nrx += dx[d]
        nry += dy[d]
        if field[nrx][nry] == "#": # 이동한 위치가 벽일 경우
            nrx -= dx[d] # 백스탭
            nry -= dy[d] # 백스탭
            break
        if field[nrx][nry] == "O": # 구멍 도착
            break
    

    
    nbx, nby = bx, by
    while True: # 위와 동일
        nbx += dx[d]
        nby += dy[d]
        if field[nbx][nby] == "#": # 벽에 닿았을 경우
            nbx -= dx[d] # 백스탭
            nby -= dy[d] # 백스탭
            break
        if field[nbx][nby] == "O": # 구멍에 골인한 경우
            break
    
    if nbx == end_x and nby == end_y: # 파란 게 들어가면 무효이므로 큐에 넣지 않기
        continue

    if nrx == nbx and nry == nby: # 위치가 겹칠 경우, 초기 위치값이 더 먼 친구를 한 칸 뒤로 물리기
        if d in (0, 1): # 상하로 이동했을 경우, x값만 비교
            if abs(rx-nrx) > abs(bx-nbx): # 빨간색이 더 많이 이동했을 경우
                nrx -= dx[d]
            else:
                nbx -= dx[d]
        if d in (2,3): # 좌우로 이동했을 경우, y값만 비교
            if abs(ry-nry) > abs(by-nby): # 빨간색이 더 많이 이동했을 경우
                nry -= dy[d]
            else:
                nby -= dy[d]
    
    # 방문 확인
    if (nrx, nry, nbx, nby) not in visited:
        visited.append((nrx, nry, nbx, nby))
        # 상하, 좌우에 따라 나뉘어서 큐에 추가하기
        if d in (0, 1): # 상 하 -> 좌우만 추가
            que.append((nrx, nry, nbx, nby, 2, cnt+1))
            que.append((nrx, nry, nbx, nby, 3, cnt+1))
        else: # 좌 우 -> 상하만 추가
            que.append((nrx, nry, nbx, nby, 0, cnt+1))
            que.append((nrx, nry, nbx, nby, 1, cnt+1))

print(res)
