from sys import stdin; input = stdin.readline
a, b = map(int,input().split())

if a*100 >= b:
    print('Yes')
else:
    print('No')