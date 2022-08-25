from collections import deque

# 수정할 아이디어 미리 메모해두기
# 각 i에서 토마토가 뻗어 나가는데
# 거리마다 지금 카운트를 세서 집어넣는 형태로 만들었음
# 근데 이러는 대신에
# 각 칸에 있는 숫자를 비교해서, 내가 더 낮으면 그걸로 바꾸는 것으로 봐야 할 듯.
# visited 에 값을 저장하는 방식이 있을 수 있고
# 그냥 필드의 값을 바꾸는 방식이 있을 수 있음.
# 내가 보기엔 후자가 더 효율적이고 짤 만 할 거 같으니까
# 집가면 한 번 짜보겠음
def bfs(start):
    que = deque()
    que.append(start)
    while que:
        x,y,cnt = que.popleft()
        visited[x][y] = cnt
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and field[nx][ny] == 0 and visited[nx][ny] == 0:
                que.append((nx,ny,cnt+1))
                field[nx][ny] = 1
# M과 N 순서로 주어짐. 그냥 그렇게 받고 x축 y축 알아서 쓰면 될 듯
M, N = map(int,input().split())

dx = [0,0,-1,1]
dy = [1,-1,0,0]
# 하나의 줄에는 가로 줄의 정보. 그냥 N개만큼 받으면 필드
field = [list(map(int,input().split())) for _ in range(N)]
# 1은 익은 토마토, 0은 익지 않은 토마토, -1은 토마토가 들어있지 않은 칸
# 모두 익어있는 상황이면 0 출력
# 모두 익지는 못하는 상황이면 -1 출력
# 기본적인 아이디어는 BFS고, 몇 일인지 확인해야 하니까 visited에 값을 추가.
# 나중에 visited 맥스 값 구하면 될 듯.
visited = [[0]*M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if field[i][j] == 1:
            bfs((i,j,0))

res = max(visited)
res2 = max(res)

for i in range(N):
    for j in range(M):
        if field[i][j] == 0:
            res2 = -1
            break
print(res2)

