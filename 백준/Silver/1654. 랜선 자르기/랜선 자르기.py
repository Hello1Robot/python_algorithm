from sys import stdin; input = stdin.readline

n, k = map(int,input().split())

cables = [int(input()) for _ in range(n)]

start = 1
end = max(cables)

while start <= end:
    mid = (start + end) // 2
    result = 0
    for cable in cables:
        result += cable // mid
    
    if result >= k:
        start = mid + 1
    
    else:
        end = mid - 1

print(start-1)