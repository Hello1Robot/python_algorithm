from sys import stdin; input = stdin.readline

n, m = map(int,input().split())
ps = list(map(int,input().split()))
sons = [[] for _ in range(n+1)]
valus = [0] * (n+1)
for i in range(1, n):
    sons[ps[i]].append(i+1) 

for j in range(m):
    s, c = map(int,input().split())
    valus[s] += c

que = [1]

while que:
    new_que = []
    for x in que:
        if sons[x]:
            for son in sons[x]:
                valus[son] += valus[x]
                new_que.append(son)
    
    que = new_que

for x in range(1,n+1):
    print(valus[x], end=' ')