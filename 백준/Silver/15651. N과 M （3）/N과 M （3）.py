def f(i,k,r):
    if i == r:
        print(*p)
    else:
        for j in range(k):
            p[i] = a[j] 
            f(i+1, k,r) 


N, R = map(int,input().split())
a = [i for i in range(1,N+1)]
used = [0] * N 
p = [0] * R
f(0, N, R)