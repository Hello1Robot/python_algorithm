from sys import stdin; input = stdin.readline
from collections import defaultdict, deque
import heapq
N = int(input())
que = []
original = []
alp = defaultdict(int)
res = 0
for _ in range(N):
    a = input().rstrip()
    original.append(a)
    heapq.heappush(que, (-len(a), deque(a)))

now = 9

while que:
    cnt, q = heapq.heappop(que)
    x = q.popleft()
    cnt += 1
    if x not in alp:
        alp[x] = now
        now -= 1
    if cnt < 0:
        heapq.heappush(que, (cnt, q))

for origin in original:
    new = []
    for i in origin:
        x = str(alp[i])
        new.append(x)
    res += int(''.join(new))

print(res)

# 반례
# 10
# ABB
# BB
# BB
# BB
# BB
# BB
# BB
# BB
# BB
# BB