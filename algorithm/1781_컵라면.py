from sys import stdin; input=stdin.readline
import heapq
N = int(input())
que = []
# 1번 안 : 데드라인 낮은거부터 쓱싹한다는 계획 폐기
# for _ in range(N):
#     dead, cup = map(int,input().split())
#     heapq.heappush(que, (dead, -cup))

# day = 0
# cups = 0
# while que:
#     de, cupramen = heapq.heappop(que)
#     if de > day:
#         day += 1
#         cups -= cupramen

# print(cups)

# 2번안 : 컵라면 많이주는 문제부터 풀기
# 이거의 경우에는 데드라인이랑 데이랑 어캐 조절하느냐가 핵심
# 아~ 헷갈려
# 뽑은 데드라인을 맥스데드라인으로 설정?
# 만약 데드라인 3인걸 먼저 뽑았어
# 그럼 그건 2개를 먼저 뽑은거란말야
# 앞에 1, 2 인 건 들어올 수 있음
# 만약 그 다음거 뽑았는데 4다?
# 그럼 자연스럽게 1, 2 비워두고 3,4 된거임
# 근데 봐봐, 3인데다 8 9 이렇게 겹칠수있음.
# 동일한 데드라인에 큰 컵라면 걸려있을 경우
# 이친구들부터 쓱싹해야함 ㅎㅎ;
# 만약 3 3 1 이순서로 컵라면이 크다 하면
# 3 3 하면 나머지 하루가 남으니까 1도 할 수 있도록 해야함
# 1. 컵라면이 맥스인 데드라인을 뽑는다.
# 해당 데드라인이 현재의 max_deadline이 된다.
# 그냥 visited 같은걸 하나 만들어서 값을 넣어야하나,,,
# 시간초과날듯? 근데 로직을 생각해보면 3 -> 1~4 사이의 공간 확인해서 빈공간에 넣기
# 1이 아니라, 하나를 박을 때마다 현재 데드라인을 체크하면서 넣어야하나? 흠
# 그럼 곤란곤란
# 뭐 이런느낌?
# visited = [0] * 2000001
# cups = 0
# for _ in range(N):
#     dead, cup = map(int,input().split())
#     heapq.heappush(que, (-cup, dead))

# while que:
#     c, d = heapq.heappop(que)
#     for i in range(d,0,-1):
#         if visited[i] == 0:
#             visited[i] = c
#             cups -= c
#             break

# print(cups)

## 역시 시간초과

# for문 계속 돌아야해서 시초날거라고 생각했음
# 저 로직을알잘딱깔쎈하게풀어야함
# 로직자체는 빈자리 넣는게 맞는데
# 굳이 for문을 돌려서 빈자리를 넣어야 하는 건 아니고
# twopointer로 최소값 최대값을 찾아서 넣는 게 맞을듯.
# 아~ 이거 진짜 변수로 잘 조지면 되는건데
# 좀 헷갈리네
# visited는 진짜아님 ㅇㅇ
# 근데 힙큐는 맞음
# max_dead = 0
# min_dead = 1e9
# cnt = 0
# for _ in range(N):
#     dead, cup = map(int,input().split())
#     heapq.heappush(que, (-cup, dead))

# while que:
#     c, d = heapq.heappop(que)
#     if d > max_dead:
#         max_dead = d



# min과 max를 초기화시키기잖아
# 3을 넣었어 그럼 max = 3 min = 3
# 2가 들어가? 이게 min보다 작으니까 min = 2
# cnt도 해야하긴 하거든? 어따쓸지 모르니까
# 3이 하나 더 들어가? 그럼 맥스랑 민은 변동없고 cnt=2지
# 1이 들어가게 하려먼 어떻게 해야 하나? max보다 cnt가 적으면 들어갈 수 있음
# min보다 value가 작으면 들어갈 수 있음
# 이러면 낮은 숫자 도저히 초기화 못시켜서 안됨

# 로직 변경
# 넣을 수 있는 거 다 집어넣음
# 만약 다음에 넣을 게 넣어둔 것의 최소값보다 크다면 최소값 빼고 그 값 집어넣기
# 이게 좀 더 힙큐다운듯?
quests = [tuple(map(int,input().split())) for _ in range(N)]
quests.sort()

for dead, cup in quests:
    heapq.heappush(que, cup)
    if dead < len(que):
        heapq.heappop(que)

print(sum(que))