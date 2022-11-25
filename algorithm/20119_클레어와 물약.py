# 같은 물약을 만드는 레시피가 여러 개 일 수 있으므로
# 그거 고려해서 다시 로직 짜야됨
# 아~ 개귀차나~

from sys import stdin; input = stdin.readline
from collections import deque

N, M = map(int,input().split())

recipes = {i:[] for i in range(1,N+1)}
needs = [0] * (N+1)
visited = [0] * (N+1)
res = set()

for _ in range(M):
    need, *el, ob = map(int,input().split())
    needs[ob] = need
    for e in el:
        recipes[e].append(ob)

K = int(input())
que = deque(list(map(int,input().split())))

while que:
    x = que.popleft()
    res.add(x)
    if not visited[x]:
        visited[x] = 1
        for r in recipes[x]:
            needs[r] -= 1
            if needs[r] == 0:
                que.append(r)
print(len(res))
res_list = sorted(list(res))
print(*res)