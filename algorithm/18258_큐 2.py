import sys
from collections import deque
N = int(sys.stdin.readline())
que = deque()
for i in range(N):
    cmd = sys.stdin.readline().strip().split()
    if cmd[0] == 'push':
        que.append(cmd[1])
    elif cmd[0] == 'pop':
        if que:
            print(que.popleft())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(que))
    elif cmd[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if que:
            print(que[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if que:
            print(que[-1])
        else:
            print(-1)