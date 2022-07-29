N = int(input())
M = int(input())
coms = [0] * (N+1)

coms[1] = 1
res = []
for _ in range(M):
    A, B = map(int, input().split())
    res.append([A, B])
res.sort(key=lambda x:x[0])
for i in range(M):
    for com in res:
        if coms[com[0]] != coms[com[1]]:
            coms[com[0]] = coms[com[1]] = 1

    
result = coms.count(1) - 1
print(result)