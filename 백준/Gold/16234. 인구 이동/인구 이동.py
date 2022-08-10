from collections import deque

def bfs(x,y):
    # 이동할 방향 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    bfs_list = []
    que = deque()
    bfs_list.append((x,y))
    que.append((x,y))

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < N and ny >= 0 and ny < N and visit[nx][ny] == 0:
                if L <=abs(field[x][y] - field[nx][ny]) <= R : # L과 R 사이
                    visit[nx][ny] = 1 # 옆마을에 방문했으면 방문했다고 표시
                    que.append((nx, ny))
                    bfs_list.append((nx,ny))
    return bfs_list


N, L, R = map(int, input().split())
field = []
for _ in range(N):
    field.append(list(map(int, input().split())))

# 일단 요구하는 값 받아왔음

# 아이디어 : 상하좌우 확인해서 밸류가 L이상 R이하로 차이나는 친구들을 확인한다.
# 그 좌표값을 리스트에 넣는다.
# 리스트에 있는 값 합쳐서 평균 내고, 꺼냈던 데로 다시 넣는다.
# L이상 R이하인 값이 없을 때까지 반복한다.
# 카운트를 출력한다.


res = 0 # 반환할 result 값 초기화

while True:
    visit = [([0] * (N+1)) for _ in range(N+1)] # 방문사실 확인할 리스트 초기화
    cnt = 0 # 인구이동이 일어나는지 안 일어나는지 확인하는 cnt
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0: # 만약 방문하지 않은 도시일 경우
                visit[i][j] = 1 # 방문했다고 표시 해주고
                city = bfs(i,j) # bfs 구동해줌. -> 문이 열린 좌표 리스트 반환
                if len(city) > 1: # 값이 두 개 이상 있으면(인구이동이 일어나면)
                    cnt = 1
                    total = 0 # 토탈값 초기화
                    for o,p in city:
                        total += field[o][p]
                    res_people = total // len(city) # 소수점 버림
                    for o, p in city:
                        field[o][p] = res_people
    if cnt == 0:
        break

    res += 1

print(res)