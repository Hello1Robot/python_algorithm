# 이전에 쓰던 거 재활용
# 결국 둘 다 짝수일 때만 상정하면 됨
# 그리디적으로 접근하면, 가로세로의 합이 홀수인 칸 중에
# 가장 값이 적은 칸을 고른 후
# 그 칸을 제외하는 완전탐색 경로를 찾으면 됨
# 결국 해당 경로 찾는 방법을 짜는 게 핵심
# 맨 위일 경우랑 맨 아래일 경우만 조심하면 되나?

# 경우 생각하기
# 가로만 생각해도 됨
# 같은 줄 or 바로 아랫줄인 경우만 생각
    # 같은 줄만 고려하려고 했었는데
    # 같은 줄만 고려할 경우, 마지막 줄이 문제가 생기고
    # 또 방향을 설정해야 하는 번거로움이 생기는데
    # 생각해보니까 짝수일 경우일 때만 일어나는 일이라서
    # 그냥 2줄을 하나의 세트로 묶어서 봐도 문제가 없었음
# 2줄을 하나의 세트로 묶어서 탐색
# 만약에 2줄 중에 최소값이 있을 경우에는
# 위아래 번갈아가면서 움직이다가
# 해당 칸만 뛰어넘어가는 형식으로 구현

from sys import stdin; input=stdin.readline

N, M = map(int,input().split())
field = [tuple(map(int,input().split())) for _ in range(N)]

res = ''
if N%2: # N이나 M 둘 중 하나가 홀수이면 무조건 전체를 돌 수 있음
    for i in range(N):
        if not i%2 :
            res += ('R'*(M-1) + 'D')
        else:
            res += ('L'*(M-1)+'D')


elif M%2: # N이나 M 둘 중 하나가 홀수이면 무조건 전체를 돌 수 있음
    for i in range(M):
        if not i%2 :
            res += ('D'*(N-1)+'R')
        else:
            res += ('U'*(N-1)+'R')


else: # 둘 다 짝수일 경우
    min_val = 1e9
    min_x, min_y = -1, -1
    for i in range(N):
        for j in range(M):
            if (i+j)%2:
                if field[i][j] < min_val:
                    min_val = field[i][j]
                    min_x, min_y = i, j
    catch = 0
    for i in range(0,N,2):
        if i == min_x or i == (min_x-1): # 이 줄이나 아랫줄에 최소점이 있으면
            catch = 1
            find = 0
            y = 0
            while y != M-1:
                if i == min_x-1 and y == min_y: # 아래가 최소점
                    res += 'RD'
                    y += 1
                    find = 1
                    
                elif i == min_x and y == min_y-1: # 오른쪽이 최소점
                    res += 'DR'
                    y += 1
                    find = 1

                else:
                    if not find:
                        res += 'DRUR'
                        y += 2
                    else:
                        res += 'RURD'
                        y += 2
            res += 'D'
                
        else:
            if catch == 0:  # 못찾았으면 오른쪽 먼저 감
                res += ('R'*(M-1) + 'D' + 'L'*(M-1) + 'D')
            else:           # 찾았으면 왼쪽 먼저 감
                res += ('L'*(M-1) + 'D' + 'R'*(M-1) + 'D')

print(res[:-1])
