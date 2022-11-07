from sys import stdin; input = stdin.readline
# from collections import deque
# def BFS(x=0, y=1):
#     que = deque()
#     que.append((x,y,3))
#     while que:
#         global res_cnt
#         x, y, c = que.popleft()
#         if x == N-1 and y == N-1:
#             res_cnt += 1
#             continue

#         if c == 1:
#             if x+1 < N and field[x+1][y] == 0:
#                 que.append((x+1, y, 1))
#                 if y+1 < N and field[x+1][y+1] == 0 and field[x][y+1] == 0:
#                     que.append((x+1, y+1, 2))
#         elif c == 2:
#             if x+1 < N and field[x+1][y] == 0:
#                 que.append((x+1, y, 1))
#             if y+1 < N and field[x][y+1] == 0:
#                 que.append((x, y+1, 3))
#                 if x+1 < N and field[x+1][y+1] == 0 and field[x+1][y] == 0:
#                     que.append((x+1,y+1,2))
#         else:
#             if y+1 < N and field[x][y+1] == 0:
#                 que.append((x, y+1, 3))
#                 if x+1 < N and field[x+1][y+1] == 0 and field[x+1][y] == 0:
#                     que.append((x+1, y+1, 2))            

def DFS(x=0, y=1, c=3):
    global res_cnt
    flag = 0 # 대각선 가능한지 확인하는 변수
    if x == N-1 and y == N-1:
        res_cnt += 1
        return

    nx = x+1
    ny = y+1

    if nx < N and ny < N and field[nx][y] == 0 and field[nx][ny] == 0 and field[x][ny] == 0:
        DFS(nx,ny,2)
        flag = 1
    
    if c == 1 or c == 2:
        if flag or (nx < N and field[nx][y] == 0): # 대각선이 가능할 경우, 굳이 한번 더 확인할 필요 없음
            DFS(nx,y,1)
    
    if c == 2 or c == 3:
        if flag or (ny < N and field[x][ny] == 0):
            DFS(x,ny,3)
            




N = int(input())
field = [tuple(map(int,input().split())) for _ in range(N)]
res_cnt = 0
# BFS()
DFS()
print(res_cnt)
# 파이프를 세로, 대각선, 가로 방향에 따라서 1, 2, 3번 상태로 나눈다.
# 1번 상태, 2번 상태, 3번 상태 각각 갈 수 있는 방향을 설정한다.
# 대각선으로 이동할 때에는 봐야할 곳 세 곳을 다 확인한다.
# 처음 파이프가 0,0 과 0,1에 놓여져 있다고 설정되어있으니까
# 시작점을 0,1로 잡고 시작한다.
# 뒤로 돌아가는 경우가 없기 때문에 굳이 visited를 설정하지 않아도 될수도?
# 코드 겹치는 부분 간소화시키자... 어휴
# 결국 셋 다 대각선은 확인하니까 대각선은 공통으로 확인