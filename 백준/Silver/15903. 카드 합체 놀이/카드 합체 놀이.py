import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int,input().split()))
heapq.heapify(nums)
for i in range(M):
    a = heapq.heappop(nums)
    b = heapq.heappop(nums)
    c = a + b
    heapq.heappush(nums, c)
    heapq.heappush(nums, c)

print(sum(nums))