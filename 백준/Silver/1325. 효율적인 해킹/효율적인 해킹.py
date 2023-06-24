from sys import stdin; input = stdin.readline
from collections import defaultdict, deque

def BFS(x):
    visited = [0]*(n+1)
    que = deque()
    visited[x] = 1
    que.append(x)
    cnt = 1
    while que:
        start = que.popleft()
        for node in tree[start]:
            if not visited[node]:
                visited[node] = 1
                cnt += 1
                que.append(node)
    return cnt
                

n, m = map(int,input().split())
tree = defaultdict(list)
result_list = [0]*(n+1)
max_result = -1
max_list = []
for _ in range(m):
    a, b = map(int,input().split())
    tree[b].append(a)

for i in range(1,n+1):
    result_list[i] = BFS(i)
    if result_list[i] > max_result:
        max_result = result_list[i]
        max_list.clear()
        max_list.append(i)
    elif result_list[i] == max_result:
        max_list.append(i)

max_list.sort()
print(*max_list)