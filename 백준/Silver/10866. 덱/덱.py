import sys
from collections import deque
N = int(input())
rst = []
que = deque(rst)
for _ in range(N):
    A = sys.stdin.readline().split()
    if A[0] == 'push_front':
        que.appendleft(A[1])
    elif A[0] == 'push_back':
        que.append(A[1])
    elif A[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif A[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)
    elif A[0] == 'pop_front':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif A[0] == 'pop_back':
        if que:
            print(que.pop())
        else:
            print(-1)
    elif A[0] == 'size':
        print(len(que))
    elif A[0] == 'empty':
        if len(que):
            print(0)
        else:
            print(1)