def dfs(tot, nums):
    global cnt
    if tot > N:
        return
    
    if tot == N:
        cnt += 1
        if cnt == K:
            print(nums[:-1])
            exit()
    for i in (1,2,3):
        dfs(tot+i, nums+str(i)+'+')

N, K = map(int,input().split())
res_list = []
cnt = 0
dfs(0,'')
print(-1)

