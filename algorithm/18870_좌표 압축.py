import sys
input = sys.stdin.readline

# que로 돌리는 건 실패
# dict를 써보자

N = int(input())
nums = list(map(int,input().split()))
num_dict = {}
for num in nums:
    if num not in num_dict:
        num_dict[num] = 0
num_keys = list(num_dict.keys())
num_keys.sort()

for idx, val in enumerate(num_keys):
    num_dict[val] = idx


for num in nums:
    print(num_dict[num], end=' ')





# que = deque(nums)
# res = []
# for _ in range(N):
#     cnt = 0
#     a = que.popleft()
#     for i in range(N-1):
#         if que[i] < a:
#             cnt += 1
#     res.append(cnt)
#     que.append(a)

# print(*res)
