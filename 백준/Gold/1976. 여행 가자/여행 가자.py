from sys import stdin; input = stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]

def union(x,y):
    a = find(x)
    b = find(y)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = list(range(n+1))
m = int(input())
field = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if field[i][j] == 1:
            union(i+1, j+1)

plans = list(map(int,input().split()))
flag = True
pa = 0
for plan in plans:
    if not pa:
        pa = find(plan)
    
    else:
        if pa != find(plan):
            flag = False

print('YES') if flag else print('NO')