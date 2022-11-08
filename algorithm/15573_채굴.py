from sys import stdin; input=stdin.readline
import heapq
N, M, K = map(int,input().split()) # 값 받아오기
field = [list(map(int,input().split())) for _ in range(N)] # 광물필드 구성하기
visited = [[0]*M for _ in range(N)] # 방문처리할 필드 만들어놓기
que = [] # 캘 수 있는 광물을 담는 큐
for i in range(N): # 순회하면서 캘 수 있는 광물을 힙큐형식으로 집어넣기
    for j in range(M):
        if i == 0 or j == 0 or j== M-1:
            heapq.heappush(que, (field[i][j], i, j) )
            visited[i][j] = 1
cnt = 0 # 캔 광물을 세는 cnt
mx = -1 # 캐야 했던 가장 큰 광물 담아놓는 변수
while que:
    c, x, y = heapq.heappop(que) # (캘수있는)최소광물, x, y
    cnt += 1 # 꺼냈으면 카운트 올리기
    if c > mx: # 가장 큰 광물값 업데이트
        mx = c 
    if cnt == K: # 도달하면 출력 후 끝
        print(mx)
        break

    for dx, dy in ((0,1),(1,0),(-1,0),(0,-1)): # 순회하기
        nx, ny = x+dx, y+dy
        if  nx >= N or nx < 0 or ny >= M or ny < 0 or visited[nx][ny]: # 팅!
            continue
        heapq.heappush(que, (field[nx][ny], nx, ny)) # 캐고났으면 다음 캘 수 있는 광물 집어넣기
        visited[nx][ny] = 1