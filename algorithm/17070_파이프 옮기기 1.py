from sys import stdin; input = stdin.readline
from collections import deque
def BFS(x=0, y=1):
    que = deque()
    que.append((x,y,3))
    while que:
        global res_cnt
        x, y, c = que.popleft()
        if x == N-1 and y == N-1:
            res_cnt += 1
            continue

        if c == 1:
            if x+1 < N and field[x+1][y] == 0:
                que.append((x+1, y, 1))
                if y+1 < N and field[x+1][y+1] == 0 and field[x][y+1] == 0:
                    que.append((x+1, y+1, 2))
        elif c == 2:
            if x+1 < N and field[x+1][y] == 0:
                que.append((x+1, y, 1))
            if y+1 < N and field[x][y+1] == 0:
                que.append((x, y+1, 3))
                if x+1 < N and field[x+1][y+1] == 0 and field[x+1][y] == 0:
                    que.append((x+1,y+1,2))
        else:
            if y+1 < N and field[x][y+1] == 0:
                que.append((x, y+1, 3))
                if x+1 < N and field[x+1][y+1] == 0 and field[x+1][y] == 0:
                    que.append((x+1, y+1, 2))            

N = int(input())
field = [tuple(map(int,input().split())) for _ in range(N)]
res_cnt = 0
BFS()
print(res_cnt)
# 파이프를 가로, 대각선, 세로 방향에 따라서 1, 2, 3번 상태로 나눈다.
# 1번 상태, 2번 상태, 3번 상태 각각 갈 수 있는 방향을 설정한다.
# 대각선으로 이동할 때에는 봐야할 곳 세 곳을 다 확인한다.
# 처음 파이프가 0,0 과 0,1에 놓여져 있다고 설정되어있으니까
# 시작점을 0,1로 잡고 시작한다.
# 뒤로 돌아가는 경우가 없기 때문에 굳이 visited를 설정하지 않아도 될수도?
#  