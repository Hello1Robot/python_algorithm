def DFS(i,n,st):
    if i == n:
        res_set.add(st[:-1])
    else:
        for x in range(N):
            if visited[x] == 0:
                visited[x] = 1
                DFS(i+1, n, st+str(nums[x])+' ')
                visited[x] = 0


N, M = map(int,input().split())
nums = list(map(int,input().split()))
visited = [0]*N
nums.sort()
res_set = set()
DFS(0,M,'')
res_list = list(res_set)
for res in res_list:
    print(res)