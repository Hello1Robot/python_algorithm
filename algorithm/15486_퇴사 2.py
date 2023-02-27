# DP문제
# (N-i)일보다 크면 할 수 없는 일임
from sys import stdin; input=stdin.readline


N = int(input())
days = []
for i in range(N):
    pay, day = map(int,input().split())
    days.append((pay, day))

DP = [0]*N
