import heapq
import sys
input = sys.stdin.readline
que = []
N = int(input())
for _ in range(N):
    cmd = int(input())
    if cmd == 0:
        if que:
            print(heapq.heappop(que)[1])
        else:
            print(0)
    else:
        heapq.heappush(que, (abs(cmd), cmd))