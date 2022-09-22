import heapq

N = int(input())
화물차 = []
for _ in range(N):
    시작, 끝 = map(int,input().split())
    heapq.heappush(화물차, (끝, 시작))
cnt = 0
while 화물차:
    끝, 시작 = heapq.heappop(화물차)
    cnt += 1
    while 화물차:
        다음끝, 다음시작 = heapq.heappop(화물차)
        if 다음시작 >= 끝:
            heapq.heappush(화물차, (다음끝, 다음시작))
            break
print(cnt)