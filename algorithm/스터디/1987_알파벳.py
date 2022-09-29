# 기억을 더듬어 다시풀기
import sys
def DFS(x=0, y=0, cnt=1):
    global max_cnt
    max_cnt = max(max_cnt, cnt)
    if cnt == 26:
        print(26)
        exit()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        if field[nx][ny] in visited:
            continue
        visited.add(field[nx][ny])
        DFS(nx,ny,cnt+1)
        visited.remove(field[nx][ny])

dx = [0,1,0,-1]
dy = [1,0,-1,0]
N, M = map(int,sys.stdin.readline().split())
max_cnt = 0
field = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
# visited = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0,'G':0,"H":0,'I':0,'J':0,'K':0,'L':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0,'M':0,'N':0}
# visited[field[0][0]] = 1
visited = set(field[0][0])
DFS()
print(max_cnt)