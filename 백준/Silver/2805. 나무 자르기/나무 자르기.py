import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 잘라나가다가, M보다 작아지면 그 이전 값을 출력하자
woods = list(map(int, input().split()))
woods.sort(reverse=True)
start = 0
end = woods[0]
while start < end:
    gap = 0
    mid = (start + end) // 2
    for wood in woods:
        if wood > mid:
            gap += wood - mid
        else:
            break
    
    if gap >= M:
        start = mid+1
    
    else:
        end = mid

print(start-1)