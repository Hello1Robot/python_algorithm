from sys import stdin; input=stdin.readline
import heapq

N, K = map(int,input().split()) # 보석갯수 N, 가방갯수 K
jewels = [] # 보석의 (무게,가치)로 리스트 만들기
for _ in range(N):
    heapq.heappush(jewels, list(map(int,input().split()))) # 힙으로 보석 집어넣기

bags = [ int(input()) for _ in range(K)] # 가방의 허용무게로 리스트 만들기
bags.sort()
que = []
res = 0
for bag in bags:
    while jewels and bag >= jewels[0][0]: # 보석이 있고, 가방에 들어가는 크기일 때
        val = heapq.heappop(jewels)[1] # (들어가는)가치 뽑아내기
        heapq.heappush(que, -val) # 큐에 저장해두기
    if que: # 큐에 다 집어넣고 난 후, 큐에 값이 있으면
        res -= heapq.heappop(que) # 결과값에 더해주기
    elif not jewels: # 큐에 값이 없는데, 남은 보석도 없는 경우, 가방에 넣을 수 있는 보석이 없다는 것
        break

print(res) # 결과값 프린트
