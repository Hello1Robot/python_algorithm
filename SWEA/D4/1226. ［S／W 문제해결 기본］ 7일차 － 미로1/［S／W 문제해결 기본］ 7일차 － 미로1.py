from collections import deque

def bfs(start, end):
    que = deque()
    que.append(start)
    while que:
        x,y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 16 and 0 <= ny < 16 and field[nx][ny] == 0 and visited[nx][ny] == False:
                que.append((nx,ny))
                visited[nx][ny] = True
                field[nx][ny] = 1
            elif 0 <= nx < 16 and 0 <= ny < 16 and field[nx][ny] == 3:
                return 1
    return 0        
        
dx = [0,0,-1,1]
dy = [-1,1,0,0]
for test_case in range(1,11):
    N = int(input())
    # 길이는 16으로 고정
    field = [list(map(int,input())) for _ in range(16)]
    visited = [[False]*16 for _ in range(16)]
    stt_x = stt_y = 0
    end_x = end_y = 0
    for i in range(16):
        for j in range(16):
            if field[i][j] == 2:
                stt_x = i
                stt_y = j
            elif field[i][j] == 3:
                end_x = i
                end_y = j
    
    print(f'#{test_case} {bfs((stt_x,stt_y),(end_x,end_y))}')