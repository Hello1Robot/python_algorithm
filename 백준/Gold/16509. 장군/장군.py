from collections import deque

visited = [[0]*9 for _ in range(10)]
# 8가지 방향으로 움직임
moves = [(0,1,1,1),(0,1,-1,1),(0,-1,1,-1),(0,-1,-1,-1),(1,0,1,1),(1,0,1,-1),(-1,0,-1,-1),(-1,0,-1,1)]
# 왕을 뛰어넘을 수 없음


que = deque()
sang_x, sang_y = map(int,input().split())
que.append((sang_x,sang_y))
visited[sang_x][sang_y] = 1
king_x, king_y = map(int,input().split())
visited[king_x][king_y] = -1
res = -1
while que:
    x, y = que.popleft()

    for dx, dy, ddx, ddy in moves:
        nx = x + dx
        ny = y + dy
        if nx >= 10 or nx < 0 or ny >= 9 or ny < 0 or visited[nx][ny] == -1:
            continue

        nx = nx + ddx
        ny = ny + ddy

        if nx >= 10 or nx < 0 or ny >= 9 or ny < 0 or visited[nx][ny] == -1:
            continue

        nx = nx + ddx
        ny = ny + ddy
        if nx >= 10 or nx < 0 or ny >= 9 or ny < 0:
            continue
        
        if visited[nx][ny] == -1:
            print(visited[x][y])
            exit()

        visited[nx][ny] = visited[x][y] + 1
        que.append((nx,ny))

print(res)
        
