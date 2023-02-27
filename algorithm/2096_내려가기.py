from sys import stdin; input=stdin.readline

N = int(input())
# 첫번째는 1,2만 고려
# 두번째는 1,2,3 고려
# 세번째는 2,3 고려
field = [tuple(map(int,input().split())) for _ in range(N)]
fmin, smin, tmin, fmax, smax, tmax = [0]*(N+1), [0]*(N+1), [0]*(N+1), [0]*(N+1), [0]*(N+1), [0]*(N+1)

for i in range(1,N+1):
    fmin[i] = min(fmin[i-1], smin[i-1]) + field[i-1][0]
    smin[i] = min(fmin[i-1], smin[i-1], tmin[i-1]) + field[i-1][1]
    tmin[i] = min(tmin[i-1], smin[i-1]) + field[i-1][2]
    fmax[i] = max(fmax[i-1], smax[i-1]) + field[i-1][0]
    smax[i] = max(fmax[i-1], smax[i-1], tmax[i-1]) + field[i-1][1]
    tmax[i] = max(tmax[i-1], smax[i-1]) + field[i-1][2]

print(max(fmax[N], smax[N], tmax[N]), min(fmin[N],smin[N],tmin[N]))

# 메모리초과