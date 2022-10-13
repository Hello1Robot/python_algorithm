from collections import deque
# 나보다 같으면 지나갈 수 있음
# 나보다 작으면 꺼억
# 나보다 큰것만 있으면 갇혀서 못감
# 위에서부터 하면 곤란곤란
# BFS 해야될듯
# 아이디어 정리
# 아기상어카운트 만들기
# 아기상어먹이카운트 만들기
# 아기상어카운트만큼 아기상어먹이카운트가되면
# 아기상어카운트 1늘리고 아기상어먹이카운트 초기화
# 먹이 찾으면 x좌표차이, y좌표차이만큼 cnt에 더해줌
# 아기 상어 뚜루뚜뚜뚜
# 위 오른쪽 왼쪽 아래 순으로 탐색할래

# nx+ny값을 앞에다 넣고, 뒤에 nx,ny순으로 튜플 만들어서
# 만약 하나라도 생기면 뒤에 친구들 큐에 넣지 말고
# 큐에서 뽑기

def 아기상어뚜루뚜뚜뚜(i,j):
    global baby_shark_cnt
    global shark_feed_cnt
    global move_cnt
    res_list = []
    que = deque()
    que.append((i,j))
    visited = [[0]*N for _ in range(N)]
    visited[i][j] = 1
    while que:
        x,y = que.popleft()
        for c in range(4):
            nx = x + dx[c]
            ny = y + dy[c]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if not visited[nx][ny] and field[nx][ny] <= baby_shark_cnt:
                visited[nx][ny] = visited[x][y] + 1
                if 0 < field[nx][ny] < baby_shark_cnt:
                    # move_cnt += visited[x][y]
                    # shark_feed_cnt += 1
                    # field[nx][ny] = 0
                    # field[i][j] = 0
                    # if shark_feed_cnt == baby_shark_cnt:
                    #     baby_shark_cnt += 1
                    #     shark_feed_cnt = 0

                    res_list.append((visited[x][y], nx, ny))
                else:
                    que.append((nx,ny))
    if res_list:
        res_list.sort()
        move, nx, ny = res_list[0]
        move_cnt += move
        shark_feed_cnt += 1
        field[nx][ny] = 0
        field[i][j] = 0
        if shark_feed_cnt == baby_shark_cnt:
            baby_shark_cnt += 1
            shark_feed_cnt = 0
        return nx, ny
    else:
        return i,j


dx = [-1,0,0,1]
dy = [0,-1,1,0]
N = int(input())

field = [list(map(int,input().split())) for _ in range(N)]
baby_shark_cnt = 2
shark_feed_cnt = 0
move_cnt = 0
x = -1
y = -1
for a in range(N):
    for b in range(N):
        if field[a][b] == 9:
            x = a
            y = b
            break
    if x != -1 or y != -1:
        break
while True:
    nx, ny = 아기상어뚜루뚜뚜뚜(x,y)
    if nx == x and ny == y:
        break
    x, y = nx, ny

print(move_cnt)