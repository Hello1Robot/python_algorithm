N, M = map(int,input().split())

def f(i,j,N,c,g):
    if i == N:
        if c == g:
            res = filter(None, bit)
            print(*res)
    else:
        bit[i] = nums[j]
        f(i+1,j,N,c+1,g)
        f(i+1,j+1,N,c+1,g)

        bit[i] = ''
        f(i+1,j,N,c,g)
        f(i+1,j+1,N,c,g)


nums = list(range(1,N+1))
bit = [0]*N
f(0,0,N,0,M)