# two pointer
# 양쪽 끝에서 이동하면서 차이가 적어지는 거 확인하는 문제
# 세 용액이니까 처음부터 끝까지 가면서 하면 됨
from sys import stdin; input=stdin.readline

N = int(input())
nums = list(map(int,input().split()))
nums.sort()
start, end = 0, N-1
one, two, three = 0, 0, 0
min_gap = 1e10

for i in range(N-2):
    now = nums[i]
    start, end = i+1, N-1
    while start < end:
        gap = now + nums[start] + nums[end]

        if abs(gap) < min_gap:
            one = start
            two = end
            three = i
            min_gap = abs(gap)

        if gap > 0:
            end -= 1
        
        elif gap < 0 :
            start += 1
        
        else:
            break

print(nums[three], nums[one], nums[two])


