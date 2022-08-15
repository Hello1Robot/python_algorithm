N, M = map(int, input().split())
nums = list(map(int, input().split()))
max_res = -100
if M == 1:
    print(max(nums))
else:
    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            cnt += nums[i+j]
        if cnt > max_res:
            max_res = cnt

    print(max_res)