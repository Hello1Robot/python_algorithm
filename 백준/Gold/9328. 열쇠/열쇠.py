# 초기아이디어
# 대문자알파벳을 만났을 경우에도 큐에 넣어둠
# 자물쇠큐를 따로 만들어둘까?
# 그래서 큐가 비었을 경우 자물쇠큐도 확인함
# 자물쇠큐 확인하면서 열 수 있는 애가 있으면, 해당 위치 큐에 추가해줌
# (자물쇠, x좌표, y좌표) 를 넣어두면 될 것 같은데
# 순회를 어떻게 하느냐가 관건인듯
# defaultdict로 해봐도 될수도?
from string import ascii_lowercase, ascii_uppercase
from collections import deque
from collections import defaultdict
def BFS():
    global doc_cnt

    
    while que:
        x, y = que.popleft()

        for dx, dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            nx, ny = x + dx, y + dy

            if nx >= N or nx < 0 or ny >= M or ny < 0 or visited[nx][ny] == 1 or field[nx][ny] == '*':
                continue

            if field[nx][ny] == '.':
                visited[nx][ny] = 1
                que.append((nx,ny))
            
            elif field[nx][ny] == '$':
                doc_cnt += 1
                field[nx][ny] = '*'
                visited[nx][ny] = 1
                que.append((nx,ny))
            
            elif field[nx][ny] in keys:
                k = field[nx][ny]
                if keys[k] == 1:
                    field[nx][ny] = '*'
                    visited[nx][ny] = 1
                    que.append((nx,ny))
                else:
                    keys[k] = 1
                    field[nx][ny] = '.'
                    if k in door:
                        while door[k]:
                            nnx, nny = door[k].pop()
                            field[nnx][nny] = '*'
                            visited[nnx][nny] = 1
                            que.append((nnx,nny))
                    que.append((nx,ny))
            
            else:
                k = field[nx][ny].lower()
                if keys[k] == 1:
                    field[nx][ny] = '*'
                    visited[nx][ny] = 1
                    que.append((nx,ny))
                else:
                    door[k].append((nx,ny))
    
    print(doc_cnt)






lock_list = list(ascii_uppercase)

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    doc_cnt = 0
    field = [list(input()) for _ in range(N)]
    que = deque()
    door = defaultdict(list)
    keys = {}
    for alp in ascii_lowercase:
        keys[alp] = 0

    default_keys = list(input())
    if default_keys[0] != '0':
        for k in default_keys:
            keys[k] = 1

    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if i == 0 or j == 0 or i == N-1 or j == M-1:
                if field[i][j] == '.':
                    que.append((i,j))
                    visited[i][j] = 1
                elif field[i][j] == '$':
                    doc_cnt += 1
                    field[i][j] = '*'
                    visited[i][j] = 1
                    que.append((i,j))
                elif field[i][j] in keys:
                    k = field[i][j]
                    if keys[k] == 1:
                        field[i][j] = '*'
                        visited[i][j] = 1
                        que.append((i,j))
                    else:
                        keys[k] = 1
                        field[i][j] = '.'
                        if k in door:
                            while door[k]:
                                nnx, nny = door[k].pop()
                                field[nnx][nny] = '*'
                                visited[nnx][nny] = 1
                                que.append((nnx,nny))
                        que.append((i,j))
                elif field[i][j] in lock_list:
                    k = field[i][j].lower()
                    if keys[k] == 1:
                        field[i][j] = '*'
                        visited[i][j] = 1
                        que.append((i,j))
                    else:
                        door[k].append((i,j))

    BFS()
