import sys
from collections import deque
input = sys.stdin.readline

# 루트 노드부터 시작하여 깊이(depth)를 구하는 함수
def bfs(x, depth):
    c[x] = True # 방문처리
    que = deque()
    d[x] = depth
    que.append((x, depth))
    while que:
        x, depth = que.popleft()
        for i in graph[x]: # x와 이어진 노드 탐색
            if c[i]: # 방문처리했으면
                continue # 넘기기
            parent[i][0] = x  # 부모 깊이 적어두고
            c[i] = True
            d[i] = depth+1
            que.append((i, depth+1))


# 전체 부모 관계를 설정하는 함수
def set_parent():
    bfs(1, 0) # 루트노드가 1로 고정. 문제마다 루트노드가 다르게 설정되는 경우는 받아서 사용하기
    for i in range(1, LOG):
        for j in range(1, n+1):
            parent[j][i] = parent[parent[j][i-1]][i-1]

# A와 B의 최소 공통 조상을 찾는 함수
def lca(a,b):
    # a가 더 깊으면, b가 더 깊도록 변경
    if d[a] > d[b]:
        a, b = b, a
    # 깊이가 동일할 때까지 깊이 맞춰주기
    for i in range(LOG-1, -1, -1): # 2^n만큼, 큰 부분에서 작은 부분까지 계속 거슬러가는 형식으로 찾기
        if d[b] - d[a] >= (1 << i): # 비 트 연 산 자 싫 어
            b = parent[b][i]
    
    # 부모가 같아질 때 까지 거슬러 올라가기
    if a == b:
        return a
    for i in range(LOG-1, -1, -1):
        # 조상을 향해 거슬러 올라가기
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    # 이후 부모가 찾고자 하는 조상
    return parent[a][0]

LOG = 21

n = int(input())
parent = [[0] * LOG for _ in range(n+1)] # 부모 노드 정보
d = [0] * (n+1) # 각 노드까지의 깊이
c = [0] * (n+1) # 각 노드의 깊이가 계산되었는지 여부 = visited의 역할
graph = [[] for _ in range(n+1)] # 그래프 정보

for _ in range(n-1): # 이중 리스트 형식으로 해서 각 노드를 서로 잇기
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

set_parent()

m = int(input())

for i in range(m):
    a, b = map(int,input().split())
    print(lca(a, b))
