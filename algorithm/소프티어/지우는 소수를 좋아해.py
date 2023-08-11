from sys import stdin; input = stdin.readline
import heapq
import math

def BFS():
    que = []
    que.append((0, 1)) # 코스트와 시작점 집어넣기
    visited = [1000000000] * (N+1)
    visited[1] = 0

    while que:
        cst, x = heapq.heappop(que)
        if x == N:
            return cst
        
        
        for cost, node in roots[x]:
            if visited[node] > cost:
                visited[node] = cost
                heapq.heappush(que, (cost, node))
    
    return -1

def is_prime_number(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    
    return True

N, M = map(int,input().split())

roots = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, cost = map(int, input().split())
    roots[a].append((cost, b))
    roots[b].append((cost, a))

minimum_root = BFS()

while True:
    minimum_root += 1
    if is_prime_number(minimum_root):
        break

print(minimum_root)