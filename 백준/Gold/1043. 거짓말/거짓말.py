# 거짓말을 아는 사람 = 0 으로 통일하자
# 전체 순회를 두 번 해야 하나?
# 한번 할 때 유니온 -> 결과값이 0이면 그 숫자 없애는게 맞지 않나? 아니다... 이거 두 번 돌리면 달라질 수도 있어서
# 두 번 돌리는 게 맞을거같긴 해

from sys import stdin; input = stdin.readline

def find_parent(x):
    while x != parent[x] and x != -1:
        x = parent[x]
    
    return x

def union(x,y):
    a = find_parent(x)
    b = find_parent(y)
    if a == b:
        return
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int,input().split())
parties = []
parent = list(range(n+1))
_, *knowns = map(int,input().split())
for known in knowns:
    parent[known] = 0

for _ in range(m):
    _, *party = map(int,input().split())
    parties.append(party)
    for i in range(1,len(party)):
        union(party[0], party[i])


result = 0

for party in parties:
    for p in party:
        if not find_parent(p):
            break
    else:
        result += 1


print(result)