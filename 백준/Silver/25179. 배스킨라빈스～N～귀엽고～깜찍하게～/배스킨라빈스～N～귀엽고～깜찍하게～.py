N, M = map(int, input().split())
print("Can't win") if N%(M+1)==1 else print("Can win")