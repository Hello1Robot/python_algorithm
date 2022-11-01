def DFS(i,n,m,st):
    if i == n:
        print(st[:-1])
    else:
        for num in nums:
            if num >= m:
                DFS(i+1, n, num, st+str(num)+' ')


N, M = map(int,input().split())
nums = set(map(int,input().split()))
nums = list(nums)
nums.sort()
DFS(0,M,1,'')