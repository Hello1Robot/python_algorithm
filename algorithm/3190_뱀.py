# 정직한 구현 문제
# 기초적인 구현을 공부할 때 괜찮은 문제
# 문제에서 요구하는 조건을 하나하나씩 구현해 나가는 게 숙제
# 다음 칸을 확인하여, 조건에 맞는 이동을 하는 것
# 판을 만들 필요는 없음

# 시간에 따라 뱀의 방향이 변화하는 것을 고려해야 함
# 뱀이 ㄴ자나 ㄱ자로 꺾이는데, 꺾이면서 방향이 바뀌면 마지막 위치만 저장해 놓으면, 좀 헷갈릴 듯
# 그런 의미로 큐에다가 뱀의 위치를 저장해놓고, 팝 하면서 위치를 파악하는 게 어떨까싶음

# 방향이 D와 L로 표시가 되는데, 현재 방향의 위치에서 이동하는 거니까... direction을 설정해놓고, i값 파악하기

# field를 직접적으로 만들 필요가 없기 때문에, (1,1)부터 (N,N)까지가 가능하다고 범위를 설정 (0,0부터 하고싶으면 사과 위치를 받을 때 조작 필요)

from sys import stdin; input = stdin.readline
from collections import deque

def tuple_change(t):                                                        # 튜플값 첫번째는 int, 두번째는 str값이기에 변환
    a, b = t.strip().split()
    return (int(a), b,)

dr = [(0,1),(1,0),(0,-1),(-1,0)]
now_d = 0

timer = 0

N = int(input())
apples = [tuple(map(int, input().split())) for _ in range(int(input()))]    # 전체 사과 위치 받기
bites = []                                                                  # 먹은 사과 판별
nxt = [tuple_change(input()) for _ in range(int(input()))]                  # 방향 전환하는 위치 받기
next = deque(nxt)
dummy = deque()
dummy.append((1,1,))
while dummy:
    if next and next[0][0] == timer:                                        # 방향 이동 체크
        now_d += 1 if next[0][1] == 'D' else -1
        next.popleft()
    
    timer += 1
    
    x, y = dummy[-1]
    dx, dy = dr[now_d%4]
    nx, ny = x + dx, y + dy
    if nx < 1 or nx > N or ny < 1 or ny > N or (nx, ny,) in dummy:          # 벽에 부딪히거나 내 몸이면, 끝내기
        break
    
    if (nx,ny,) in apples and (nx,ny,) not in bites:                                                  # 사과 먹었는지 판별
        bites.append((nx,ny,))
        dummy.append((nx,ny,))
    
    else:                                                                   # 사과 없으면, 꼬리 줄이기
        dummy.append((nx,ny,))
        dummy.popleft()

print(timer)









