N, M = map(int, input().split())

rst = [1000001] * (M*2)

rst[N] = 0

rst[N+1] = 1

rst[N*2] = 1

for i in range(N+2, M*2):

    if i % 2:

        rst[i] = rst[i-1] + 1

    else:

        a = rst[i//2]+1

        b = rst[i-1]+1

        rst[i]=min(a,b)

print(rst[M])