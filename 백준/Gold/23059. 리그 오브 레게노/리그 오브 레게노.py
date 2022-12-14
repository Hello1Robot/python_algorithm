from sys import stdin; input=stdin.readline
from collections import deque
# import heapq

N = int(input())
# 문자열 받아오는거니까 strip 꼭 하기
# N개를 받아오니까 최대 2n개까지 나올 수 있음
# 정리 먼저 하자
# 앞에 나오는 아이템은 뒤의 아이템에 선행되는 아이템
# 그래서 앞에 나오는 아이템을 딕셔너리에 추가
# 그런 다음 거기에다가 뒤에 나오는 아이템 집어넣음
# 만약 딕셔너리의 키값에 뒤에 나오는 아이템이 없다면 만들기(안해도되나?)
# 숫자세는 딕셔너리도 하나 만들어서, 뒤에 나오는 아이템에 선행 아이템 세기
# 선행 아이템이 없는 친구부터 제작하기.

# 원래는 큐에서 뽑으면서 프린트 해야 하는데
# 이번 문제는 사이클이 형성 될 가능성이 있기 때문에
# 별도의 res 리스트에 넣어두고, 사이클 판별이 끝나면 출력하기
후행템들 = {}
선행템갯수 = {}
결과담는리스트 = []
힙큐 = []
덱 = deque()
for _ in range(N):
    선행템, 후행템 = input().rstrip().split()
    if 선행템 not in 후행템들:
        후행템들[선행템] = []
        후행템들[선행템].append(후행템)
    else:
        후행템들[선행템].append(후행템)
    if 후행템 not in 후행템들:
        후행템들[후행템] = []
    
    if 후행템 not in 선행템갯수:
        선행템갯수[후행템] = 1
    else:
        선행템갯수[후행템] += 1
    
    if 선행템 not in 선행템갯수:
        선행템갯수[선행템] = 0

for 선행, 갯수 in 선행템갯수.items():
    if 갯수 == 0:
        # heapq.heappush(힙큐, (1,선행))
        덱.append((1,선행))

while 덱:
    # 카운트, 지금산템 = heapq.heappop(힙큐)
    카운트, 지금산템 = 덱.popleft()
    결과담는리스트.append((카운트,지금산템))
    카운트+=1
    for 뒷템 in 후행템들[지금산템]:
        선행템갯수[뒷템] -= 1
        if 선행템갯수[뒷템] == 0:
            # heapq.heappush(힙큐, (카운트,뒷템))
            덱.append((카운트, 뒷템))
결과담는리스트.sort()
if sum(선행템갯수.values()) > 0:
    print(-1)
else:
    for 카운터, 산템들 in 결과담는리스트:
        print(산템들)
