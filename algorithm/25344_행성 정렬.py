def 정렬(a,b):
    while a:
        a, b = b%a, a
    return b

N = int(input())
nums = list(map(int,input().split()))

if N <= 3:
    print(nums[0])
else:
    mins = nums[0]*nums[1]//정렬(nums[0],nums[1])
    for i in range(1,N-2):
        now = 정렬(nums[i],mins)
        mins = nums[i]*mins//now
    print(mins)
