from sys import stdin; input=stdin.readline
N, M, K = map(int,input().split())
gap = (N*M)-K
print(max(gap, 0))