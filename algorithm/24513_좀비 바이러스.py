# 문제 포인트는 3으로 변한 마을을 어떻게 처리할것인가?
# 3으로 변해도 이전에 처리한 결과가 que에 들어갈 것
# 해당 큐가 나올 때, 일일히 3인지 확인하지 않고
# 해당 큐를 종료할 수 있게 하고 싶은데
# 막 생각나지는 않으니까 일단 구현

# 반복 종료 조건 설정
# que가 비었거나 change가 0이거나.

from sys import stdin; input=stdin.readline

N, M = map(int,input().split())


field = [list(map(int,input().split()) for _ in range(N))]
now_que = []
next_que = []
cnt_list  = [0, 0, 0, 0] # 순서대로 change, 1번, 2번, 3번
moves = [(0,1),(1,0),(-1,0),(0,-1)]

for i in range(N):
    for j in range(M):
        if field[i][j] == 1 or field[i][j] == 2:
            now_que.append((field[i][j], i, j))
            cnt_list[field[i][j]] += 1

while now_que:
    for v, x, y in now_que:
        