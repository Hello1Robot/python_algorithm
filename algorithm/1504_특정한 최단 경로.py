# 아껴두고 내일 풀자...

import sys
import heapq
input = sys.stdin.readline

INF = 200000000
N, E = map(int,input().split())
field = [[INF]*(N+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j:
            field[i][j] = 0

for _ in range(E): # 양방향 그래프이므로 
    start, end, cost = map(int,input().split())
    field[start][end] = cost
    field[end][start] = cost

경유지, 도착지 = map(int,input().split())