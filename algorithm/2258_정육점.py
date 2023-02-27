from sys import stdin; input = stdin.readline
from collections import deque
N, M = map(int,input().split())
meats = deque()
for _ in range(N):
    gram, price = map(int,input().split())
    meats.append([price, gram, 0])
meats.sort()
res = -1

while meats:
    p, g, r = meats.popleft()
    if g+r >= M:
        res = p
        break
    
    if meats:
        if meats[0][0] > p:
            meats[0][2] += g+r

                    
            

print(res)
