import sys
import heapq
input = sys.stdin.readline
N = int(input())
meeting = []
for i in range(N):
    A, B = map(int, input().split())
    heapq.heappush(meeting, (B,A))
cnt = 1
while meeting:
    end, start = heapq.heappop()
    
