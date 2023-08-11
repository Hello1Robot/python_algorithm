
from sys import stdin; input = stdin.readline

def BFS(N, M, K, field):
    visited = [[K+1] * M for _ in range(N)]
    dr = [(0,1),(1,0),(-1,0),(0,-1)]
    visited[0][0] = 0
    que = [(0,0,)]
    turn = 1
    while que:
        new_que = []

        for x, y in que:
            if x == N-1 and y == M-1:
                return turn
            
            for dx, dy in dr:
                nx, ny = x + dx, y + dy
                
                if nx >= N or nx < 0 or ny >= M or ny < 0:
                    continue
                
                if turn % 2:
                    nw = int(field[nx][ny]) + visited[x][y]

                    if nw < visited[nx][ny]:
                        visited[nx][ny] = nw
                        new_que.append((nx, ny))
                else:
                    if field[nx][ny] == '0' and visited[x][y] < visited[nx][ny]:
                        visited[nx][ny] = visited[x][y]
                        new_que.append((nx,ny))
                    elif field[nx][ny] == '1' and visited[x][y]+1 < visited[nx][ny]:
                        new_que.append((x,y))

        que = new_que
        turn += 1

    return -1



N, M, K = map(int,input().split())
field = [input().rstrip() for _ in range(N)]

print(BFS(N,M,K,field))

