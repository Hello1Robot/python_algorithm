N = int(input())
nums = list(map(int,input().split()))
max_cnt = 0
cnt1 = 0
cnt2 = 0
for i in range(N-1):
    if nums[i] >= nums[i+1]:
        cnt1 += 1
    else:
        if cnt1 > max_cnt:
            max_cnt = cnt1
        cnt1 = 0
    if nums[i] <= nums[i+1]:
        cnt2 += 1
    else:
        if cnt2 > max_cnt:
            max_cnt = cnt2
        cnt2 = 0
if cnt1 > max_cnt:
    max_cnt = cnt1
if cnt2 > max_cnt:
    max_cnt = cnt2
print(max_cnt+1)