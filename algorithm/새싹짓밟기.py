import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    [input() for _ in range(m)]
    print(n-1)