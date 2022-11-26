from sys import stdin; input=stdin.readline
N = int(input())
tot = 0
for i in range(N):
    tot += int(input())

print(tot - N + 1)