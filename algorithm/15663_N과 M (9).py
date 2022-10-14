def 순열(i,n,k):
    if i == k:
        if p not in res_list:
            res_list.append(p[:])
            print(*p)
    else:
        for j in range(n):
            if not used[j]:
                used[j] = 1
                p[i] = a[j]
                순열(i+1,n,k)
                used[j] = 0

N, K = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
used = [0]*N
p = [0]*K
res_list = []
순열(0,N,K)
