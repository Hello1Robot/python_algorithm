N, M = map(int,input().split())

def f(i,N,c,g):
    if i == N:
        if c == g:
            res = filter(None, bit)
            print(*res)
    else:
        bit[i] = nums[i]
        f(i+1,N,c+1,g)
        bit[i] = ''
        f(i+1,N,c,g)


nums = list(range(1,N+1))
bit = [0]*N
f(0,N,0,M)