N = int(input())
nums = list(map(int, input().split()))

res_list = []
max_res = 0
for i in range(N):
    for j in range(1,N):
        if i < j:
            a = nums[i:j]
            x = sum(a)
            if x > max_res:
                max_res = x
    res_list.append(max_res)

res = max(res_list)
print(res)
    