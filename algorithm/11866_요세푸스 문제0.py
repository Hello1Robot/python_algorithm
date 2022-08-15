from collections import deque
# 아이디어 먼저 정리
# deque를 사용해서
# popleft로 갯수만큼 꺼내고 뒤로 넣기

N, K = map(int, input().split())
nums = list(range(1, N+1))
que = deque(nums)
cnt = 1
res_list = []
while que:
    if (cnt % K) == 0:
        b = que.popleft()
        res_list.append(b)
    else:
       a = que.popleft()
       que.append(a)


    cnt += 1

print('<', end='')
for i in range(len(res_list)-1):
    print(res_list[i], end=', ')
print(f'{res_list[-1]}>')