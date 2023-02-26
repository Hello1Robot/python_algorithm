# 기본적인 생각
# 왔던 방향으로 다시 가는 건 비효율적 -> 제거
# 즉 이전턴에 왼쪽으로 떼굴 했으면 다음턴엔 왼쪽오른쪽 떼굴 X -> 결국 위아래 떼굴만 함
# 동시 떼굴이라서 조금 어려움... 왼쪽이 R로 막혀있으면 왼쪽으로 먼저 못 감.
# 따로 떼굴떼굴 굴리고, 먼저 도착한 친구만 판별하도록 로직 짜기
# 경우의 수 어떻게 해야할까? 서로 한 칸씩 움직이게 시뮬레이션 해야하나
# 빨구 파구는 딱 한 개. 그래서 좌표값 + 이전 방향만 가져가면 될 듯?
# 그래서 함수에서 요구하는 게 (리스트), 빨구위치, 파구위치, 방향, 횟수 정도?
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

    if cnt > 10: # 10번 했는데 못찾았으면 종료
        break

    if rx == end_x and ry == end_y: # 빨간 게 도착했으면
        res = cnt
        break
    
    # 이동 거리를 판별하기 위해 초기 위치값을 복사해서 새로운 변수 생성
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

    # 빨간색이 구멍에 들어가면 끝나게 하고 싶었지만, 문제 조건 중에
    # 파란 공이 같이 들어갈 경우는 인정하지 않기 때문에
    # 해당 조건을 판별해야 해서 더 진행
    
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
