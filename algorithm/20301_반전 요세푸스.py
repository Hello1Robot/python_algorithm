from collections import deque
# 아이디어 먼저 정리
# deque를 사용해서
# popleft로 갯수만큼 꺼내고 뒤로 넣기
# A번째 횟수마다 방향을 바꾸기

N, K, M = map(int, input().split())
nums = list(range(1, N+1))
que = deque(nums)
flag = 1
kill = 0
while que:
    que.rotate(-(K))
    if flag == 1:
        print(que.pop())
    else:
        print(que.popleft())
    kill += 1
    if kill == M:
        kill = 0
        K = K * -1
        flag = flag * -1