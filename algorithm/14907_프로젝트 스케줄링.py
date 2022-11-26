from sys import stdin; input = stdin.readline
from collections import deque

alp = {'A':[],'B':[],'C':[],'D':[],'E':[],'F':[],'G':[],'H':[],'I':[],'J':[],'K':[],'L':[],'M':[],'N':[],'O':[],'P':[],'Q':[],'R':[],'S':[],'T':[],'U':[],'V':[],'W':[],'X':[],'Y':[],'Z':[]}
needs = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
costs = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}
tot = {'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'J':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0}

que = deque()
while True:
    try:
        start, cst, *els = input().split()
        cst = int(cst)
        costs[start] = cst
        if els:
            els = list(els[0])
            needs[start] += len(els)
            for e in els:
                alp[e].append(start)
        else:
            que.append(start)
            tot[start] = cst
    except:
        break

while que:
    x = que.popleft()
    c = tot[x]
    for i in alp[x]:
        tot[i] = max(tot[i], c+costs[i])
        needs[i] -= 1
        if needs[i] == 0:
            que.append(i)


print(max(tot.values()))
