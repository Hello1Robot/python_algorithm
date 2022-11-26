from sys import stdin; input = stdin.readline
from collections import deque

T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    times = tuple(map(int,input().split())) # 짓는 데 필요한 시간
    tot_times = [0]*(N+1) # 이전 것까지 포함해서 걸린 시간
    needs = [0]*(N+1) # 짓기 위해 필요한 건물 수
    nodes = {i:[] for i in range(1,N+1)}
    for _ in range(K):
        a, b = map(int,input().split())
        nodes[a].append(b)
        needs[b] += 1
    
    last = int(input())
    
    que = deque()
    for i in range(1,N+1):
        if needs[i] == 0:
            que.append(i)
            tot_times[i] = times[i-1]
    
    while que:
        start = que.popleft()
        pre_time = tot_times[start]
        if start == last:
            print(pre_time)
            break
        for x in nodes[start]:
            next_time = pre_time + times[x-1]
            tot_times[x] = max(tot_times[x], next_time)
            needs[x] -= 1
            if needs[x] == 0:
                que.append(x)