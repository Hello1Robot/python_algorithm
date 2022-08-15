from collections import deque
# 아이디어 먼저 정리
# deque를 사용해서
# popleft로 갯수만큼 꺼내고 뒤로 넣기
# A번째 횟수마다 방향을 바꾸기

N, K, A = map(int, input().split())
nums = list(range(1, N+1))
que = deque(nums)
cnt = 1
switch = 1
kill = 0
while que:

    if (cnt % K) == 0:
        b = que.popleft()

        print(b)
    else:
        a = que.popleft()
        que.append(a)


    if kill != 0 and kill % (A*K) == 0:
        que.reverse()
        print(que)
    cnt += 1
    kill += 1


