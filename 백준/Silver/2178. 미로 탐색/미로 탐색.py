from collections import deque

def path_find(x,y):
    que= deque()
    que.append((x,y))

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if field[nx][ny] == 0:
                continue
            if field[nx][ny] == 1:
                field[nx][ny] = field[x][y] + 1
                que.append((nx,ny))
    return field[-1][-1]


N, M = map(int, input().split())
field = []
for i in range(N):
    field.append(list(map(int, input())))

# 이동할 방향 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(path_find(0,0))