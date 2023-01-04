N, M = map(int,input().split())

dep = N / 100 * (100-M)

[print(0) if dep >= 100 else print(1)]