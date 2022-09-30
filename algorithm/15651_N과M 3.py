def f(i,k,r):
    if i == r:
        print(*p)
    else:
        for j in range(k):
            p[i] = a[j]     # p[i]는 a[j]로 결정
            f(i+1, k,r)       # p[i+1] 값을 결정하러 이동


N, R = map(int,input().split())
a = [i for i in range(1,N+1)]
used = [0] * N 
p = [0] * R
f(0, N, R)