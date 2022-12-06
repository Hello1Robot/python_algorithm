from sys import stdin; input=stdin.readline
import heapq
N = int(input())

minimum = []
maximum = []
for _ in range(N):
    num = int(input())
    if len(minimum) == len(maximum):
        heapq.heappush(maximum, -num)
    else:
        heapq.heappush(minimum, num)
    
    if minimum and minimum[0] < -maximum[0]:
        x = heapq.heappop(minimum)
        y = heapq.heappop(maximum)
        heapq.heappush(minimum, -y)
        heapq.heappush(maximum, -x)
    
    print(-maximum[0])
    