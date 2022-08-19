from collections import deque
N = int(input())
cards = list(range(1,N+1))
que = deque(cards)

while que:
    if len(que) != 1:
        que.popleft()
        que.rotate(-1)
    else:
        print(que.pop())