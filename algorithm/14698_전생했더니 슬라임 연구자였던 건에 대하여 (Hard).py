import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    nums = list(map(int,input().split()))
    if N == 1:
        print(1)
        continue
    heapq.heapify(nums)
    res = 1
    while len(nums) != 1:
        a = heapq.heappop(nums)
        b = heapq.heappop(nums)
        c = a*b
        res *= c
        heapq.heappush(nums, c)
    
    print(res%1000000007)