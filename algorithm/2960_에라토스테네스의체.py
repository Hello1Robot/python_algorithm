# DP와 visited를 만들어서 채워넣자
N, K = map(int,input().split())
DP = list(range(N+1))
visited = [0]*(N+1)
res = 0
for i in range(2,N+1):
    if DP[i] != 0:
        cnt=i
        while cnt <= N:
            if DP[cnt] != 0:
                DP[cnt] = 0
                res += 1
            if res == K:
                print(cnt)
                exit()
            cnt += i

            
