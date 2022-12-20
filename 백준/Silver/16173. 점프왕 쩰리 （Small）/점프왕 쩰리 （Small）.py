from sys import stdin; input=stdin.readline
from collections import deque
# 쩰리는 오른쪽과 아래로만 움직이기 때문에 visited가 필요가 없다.
# 틀리는 이유 : 젤리는 지그재그로 못움직인대...
def BFS(x=0, y=0):
    que = deque()
    que.append((x,y)) # 시작, 끝, 카운트 넣어줌
    while que:
        x, y = que.popleft()
        
        if field[x][y] == -1:
            print('HaruHaru')
            exit()
        

        for dx, dy in [(0,1),(1,0)]:
            nx = x + dx*field[x][y]
            ny = y + dy*field[x][y]          
            if nx >= N or nx < 0 or ny >= N or ny < 0 or field[nx][ny] == 0:
                continue
            que.append((nx,ny))

    print('Hing')




N = int(input())
field = [tuple(map(int,input().split())) for _ in range(N)]
if field[0][0] == 0:
    print('Hing')
    exit()
BFS()