import heapq
import sys
input = sys.stdin.readline

N = int(input())
회의실 = []
for _ in range(N):
    시작, 끝 = map(int,input().split())
    heapq.heappush(회의실, (끝, 시작))
cnt = 0
while 회의실:
    끝, 시작 = heapq.heappop(회의실)
    cnt += 1
    while 회의실:
        다음끝, 다음시작 = heapq.heappop(회의실)
        if 다음시작 >= 끝:
            heapq.heappush(회의실, (다음끝, 다음시작))
            break
print(cnt)