# Union - find 를 구현해야 하는 기초적인 문제
# 0일 땐 유니온, 1일 땐 find 비교
from sys import stdin, setrecursionlimit; input = stdin.readline; setrecursionlimit(10**8)

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    
    return parents[x]

def union(x, y):
    a = find(x)
    b = find(y)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

n, m = map(int,input().split()) # 노드 범위, 쿼리 수
parents = list(range(n+1))
for _ in range(m):
    com, a, b = map(int,input().split())
    if not com:
        union(a,b)
    else:
        [print("YES") if find(a)==find(b) else print("NO")]