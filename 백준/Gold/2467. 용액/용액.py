# two pointer
# 양쪽 끝에서 이동하면서 차이가 적어지는 거 확인하는 문제
from sys import stdin; input=stdin.readline

N = int(input())
nums = list(map(int,input().split()))
nums.sort()
start, end = 0, N-1
one, two = 0, 0
min_gap = 1e10

while start < end:
    gap = nums[start] + nums[end]

    if abs(gap) < min_gap:
        one = start
        two = end
        min_gap = abs(gap)

    if gap > 0:
        end -= 1
    
    elif gap < 0 :
        start += 1
    
    else:
        break

print(nums[one], nums[two])


