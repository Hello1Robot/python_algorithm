def DFS(i,n,m,st):
    if i == n:
        print(st[:-1])
    else:
        for x in range(m,N+1):
            DFS(i+1, n, x, st+str(x)+' ')


N, K = map(int,input().split())
DFS(0,K,1,'')