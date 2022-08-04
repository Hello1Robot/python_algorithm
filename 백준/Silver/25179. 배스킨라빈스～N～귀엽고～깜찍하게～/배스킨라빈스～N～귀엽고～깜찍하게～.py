N, M = map(int, input().split())

if N % (M+1) == 1:
    print("Can't win")
else:
    print("Can win")