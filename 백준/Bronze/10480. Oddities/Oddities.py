from sys import stdin; input = stdin.readline

n = int(input())
for _ in range(n):
    a = int(input())
    [print(f'{a} is odd') if a%2 else print(f'{a} is even')]
        