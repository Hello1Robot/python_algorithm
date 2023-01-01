from sys import stdin; input=stdin.readline
import heapq

N = int(input())
tasks = [tuple(map(int,input().split())) for _ in range(N)]
tasks.sort()
que = []
for day, score in tasks:
    heapq.heappush(que, score)
    
    if len(que) > day:
        heapq.heappop(que)

print(sum(que))
    
    