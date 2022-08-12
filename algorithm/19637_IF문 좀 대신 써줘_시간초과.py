N, M = map(int, input().split())
if_dict = {}
for _ in range(N):
    a, b = input().split()
    if_dict[a] = int(b)
quest = []
for i in range(M):
    x = int(input())
    for ke, va in if_dict.items():
        if x <= va:
            print(ke)
            break
