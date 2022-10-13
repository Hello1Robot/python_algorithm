# 양이나 늑대를 만나면 방문처리하고 큐를 넣고 양과 늑대카운트를 올린다.
# 다 돌고나서 양과 늑대카운트를 리턴
# 만약 양카운트가 늑대카운트보다 크다면 양의 갯수만 더해줌
# 반대라면, 늑대의 갯수만 더해줌
# 출력
from collections import deque
def 양과늑대(x,y):
    que = deque()
    sheep_cnt = 0
    wolf_cnt = 0
    if field[x][y] == 'o':
        sheep_cnt = 1
    elif field[x][y] == 'v':
        wolf_cnt = 1
    field[x][y] = -1
    que.append((x,y))
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= M or ny < 0:
                continue

            if field[nx][ny] == 'o':
                sheep_cnt += 1
                field[nx][ny] = -1
                que.append((nx,ny))
            elif field[nx][ny] == 'v':
                wolf_cnt += 1
                field[nx][ny] = -1
                que.append((nx,ny))
            elif field[nx][ny] == '0':
                field[nx][ny] = -1
                que.append((nx,ny))

    return (sheep_cnt, wolf_cnt)                
    
dx = [0,0,-1,1]
dy = [-1,1,0,0]
N, M = map(int,input().split())
field = [list(input().replace('.', '0')) for _ in range(N)]
total_sheep = 0
total_wolves = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == 'o' or field[i][j] == 'v':
            sheep, wolf = 양과늑대(i,j)
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolves += wolf


print(total_sheep, total_wolves)
