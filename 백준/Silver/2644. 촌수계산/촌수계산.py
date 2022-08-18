def dfs(start, cnt):
    dfs_list.append(start)
    cnt += 1
    if start == s:
        res.append(cnt)
    for y in range(len(graph[start])):
        if graph[start][y]  == 1 and (y not in dfs_list):
            dfs(y, cnt)

# 기본적으로 촌수계산 -> 단방향
# 촌수관계가 없다(노드가 이어지지 않는다) = -1 출력
N = int(input()) # 촌수계산을 해야 할 전체 사람의 수
m, s = map(int, input().split()) # m과 s의 관계찾기(촌수)
case = int(input()) # 노드의 갯수
graph = [[0]*(N+1) for _ in range(N+1)] # N * N 의 2차원 그래프
for _ in range(case): # 노드번호 그래프에 입력
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1
dfs_list = []
res = []
dfs(m, 0)
if s in dfs_list:
    print(res[0]-1)
else:
    print(-1)