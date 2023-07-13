# 힙큐를 쓰면, 3차원 visited가 필요할까?
# 방문 여부는 확인해야 하니까 필요는 하겠다
# 그럼 2차원으로 만들어서 level을 표시하고
# 해당 레벨보다 낮으면 등록되게?
# 이게 맞는듯 ㅇㅇ

from sys import stdin; input = stdin.readline

def BFS(N, M, K, field):
    visited = [[K+1] * M for _ in range(N)]
    dr = [(0,1),(1,0),(-1,0),(0,-1)]
    visited[0][0] = 0
    que = [(1,0,0,)]
    while que:
        new_que = []
        for level, x, y in que:
            if x == N-1 and y == M-1:
                return level
            
            for dx, dy in dr:
                nx, ny = x + dx, y + dy
                
                if nx >= N or nx < 0 or ny >= M or ny < 0:
                    continue
                
                nw = int(field[nx][ny]) + visited[x][y]

                if nw < visited[nx][ny]:
                    visited[nx][ny] = nw
                    new_que.append((level+1, nx, ny))

        que = new_que

    return -1



N, M, K = map(int,input().split())
field = [input().rstrip() for _ in range(N)]

print(BFS(N,M,K,field))