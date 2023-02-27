from sys import stdin; input=stdin.readline
from math import ceil
import heapq
T = int(input())
for _ in range(T):
    N = int(input())
    nums = []
    repeat = ceil(N/10)
    for _ in range(repeat):
        numbers = list(map(int,input().split()))
        nums += numbers

    minimum = []
    maximum = []
    res = []
    for i in range(N):
        num = nums[i]
        if len(minimum) == len(maximum):
            heapq.heappush(maximum, -num)
        else:
            heapq.heappush(minimum, num)
        
        if minimum and minimum[0] < -maximum[0]:
            x = heapq.heappop(minimum)
            y = heapq.heappop(maximum)
            heapq.heappush(minimum, -y)
            heapq.heappush(maximum, -x)
        
        if i % 2:
            continue
        res.append(-maximum[0])

    print(len(res))
    for x in range(len(res)):
        print(res[x], end=' ')
        if x % 10 == 9:
            print()
    