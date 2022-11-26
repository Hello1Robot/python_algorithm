from sys import stdin
from collections import deque
input = stdin.readline

N = int(input())
if N == 1:
    print(-1)
    exit()
nums = list(map(int,input().split()))
que = deque(nums)
stk = []
while que:
    stk.append(que.popleft())
    while que:
        if que[0] <= stk[-1]:
            stk.append(que.popleft())
        else:
            
