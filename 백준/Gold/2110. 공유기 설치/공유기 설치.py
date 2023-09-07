from sys import stdin; input = stdin.readline

n, m = map(int,input().split())
hs = [int(input()) for _ in range(n)]
hs.sort()
start = 0
end = hs[-1]
while start <= end:
    mid = (start + end) // 2
    idx = hs[0]
    cnt = 1
    for i in range(1,n):
        if hs[i]-idx >= mid:
            cnt += 1
            idx = hs[i]
    
    if cnt >= m:
        start = mid + 1
    
    else:
        end = mid - 1

print(start-1)