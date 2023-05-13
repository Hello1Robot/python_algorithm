from sys import stdin; input = stdin.readline

T = int(input())

while T > 0 :
    a, b, c = map(int, input().split())
    print(min(a, min(b, c)))
    T -= 1