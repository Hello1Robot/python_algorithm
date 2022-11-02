from collections import deque
def BFS(start, cnt):
    que = deque()
    que.append((start, cnt))
    while que:
        x, c = que.popleft()
        if x > K:
            continue
        if x == K:
            return c
        que.append((2*x, c+1))
        a = int(str(x)+'1')
        que.append((a, c+1))
    return -1


N, K = map(int,input().split())

print(BFS(N, 1))