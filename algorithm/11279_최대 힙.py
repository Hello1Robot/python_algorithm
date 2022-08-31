import heapq
import sys
input = sys.stdin.readline
N = int(input())
prh = []
for i in range(N):
    cmd = int(input())
    if cmd == 0:
        if prh:
            print(heapq.heappop(prh)[1])
        else:
            print(0)
    else:
        heapq.heappush(prh, (-cmd,cmd))
