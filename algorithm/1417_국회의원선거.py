# 우선순위 큐를 이용해서 풀어보자
import sys
import heapq
input = sys.stdin.readline
N = int(input())
다솜이 = int(input())
if N == 1:
    print(0)
    exit()
후보들 = []
매수 = 0
for _ in range(N-1):
    후보 = int(input())
    heapq.heappush(후보들, (-후보,후보))

while True:
    강력한후보 = heapq.heappop(후보들)[1]
    if 다솜이 > 강력한후보:
        break
    else:
        다솜이 += 1
        강력한후보 -= 1
        heapq.heappush(후보들, (-강력한후보, 강력한후보))
        매수 += 1
    
print(매수)
