def BFS(n, m, maps):
    que = []
    que.append((0,0))
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    level = 1
    while que:
        new_que = []
        for x, y in que:
            if x == n-1 and y == m-1:
                return level

            for dx, dy in [(-1,0),(0,-1),(1,0),(0,1)]:
                nx = x + dx
                ny = y + dy

                if nx >= n or nx < 0 or ny >= m or ny < 0 or visited[nx][ny]:
                    continue
                
                if maps[nx][ny] == 1:
                    visited[nx][ny] = 1
                    new_que.append((nx,ny))
        
        que = new_que
        level += 1


    return -1

def solution(maps):
    return BFS(len(maps), len(maps[0]), maps)