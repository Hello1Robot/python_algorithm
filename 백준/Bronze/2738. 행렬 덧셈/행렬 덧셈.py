N, M = map(int,input().split())
field = [list(map(int,input().split())) for _ in range(N)]

for i in range(N):
    nums = list(map(int,input().split()))
    for j in range(M):
        field[i][j] += nums[j]

for li in field:
    print(*li)