import sys
import heapq
sys.stdin.readline

H, T, N = map(int,input().split())
giants = []
for _ in range(H):
    heapq.heappush(giants, -(int(input())))

cnt = 0
while cnt < N:
    tall_giant = heapq.heappop(giants)
    if -(tall_giant) < T or -tall_giant == 1:
        heapq.heappush(giants, tall_giant)
        break
    ppong = int(tall_giant/2)
    heapq.heappush(giants, ppong)
    cnt += 1

tall_giant = -(heapq.heappop(giants))
if tall_giant >= T:
    print('NO')
    print(tall_giant)
else:
    print('YES')
    print(cnt)


