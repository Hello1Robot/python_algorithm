def DFS(i,n):
    if i == n:
        res_set.add(tuple(rst[:]))
    else:
        for x in range(N):
            if visited[x] == 0:
                visited[x] = 1
                rst.append(nums[x])
                DFS(i+1, n)
                rst.pop()
                visited[x] = 0


N, M = map(int,input().split())
nums = list(map(int,input().split()))
visited = [0]*N
nums.sort()
res_set = set()
rst = []
DFS(0,M)
res_list = list(res_set)
res_list.sort()
for res in res_list:
    print(*res)