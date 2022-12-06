from sys import stdin; input=stdin.readline
import heapq

N, K = map(int,input().split()) # 보석갯수 N, 가방갯수 K
jewels = [] # 보석의 (무게,가치)로 리스트 만들기
for _ in range(N):
    heapq.heappush(jewels, list(map(int,input().split())))

bags = [ int(input()) for _ in range(K)] # 가방의 허용무게로 리스트 만들기
bags.sort()
que = []
res = 0
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        val = heapq.heappop(jewels)[1]
        heapq.heappush(que, -val)
    if que:
        res -= heapq.heappop(que)
    elif not jewels:
        break

print(res)
