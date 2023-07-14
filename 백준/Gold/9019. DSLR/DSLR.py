# 각 명령어 모듈화 시키기
from sys import stdin; input = stdin.readline

def D(x):
    return (2 * int(x)) % 10000

def S(x):
    if x == 0:
        return 9999
    else:
        return x-1

def L(x):
    new_x = str(x).zfill(4)
    return int(new_x[1]+new_x[2]+new_x[3]+new_x[0])

def R(x):
    new_x = str(x).zfill(4)
    return int(new_x[3]+new_x[0]+new_x[1]+new_x[2])

def BFS(n,e):
    que = [(n,'')]
    visited = [0] * 10000
    visited[n] = 1
    while que:
        new_que = []

        for x, rt in que:
            if x == e:
                return rt
            
            d, s, l, r = D(x), S(x), L(x), R(x)
            if not visited[d]:
                visited[d] = 1
                new_que.append((d, rt+'D'))
            if not visited[s]:
                visited[s] = 1
                new_que.append((s, rt+'S'))
            if not visited[l]:
                visited[l] = 1
                new_que.append((l, rt+'L'))
            if not visited[r]:
                visited[r] = 1
                new_que.append((r, rt+'R'))
        
        que = new_que

T = int(input())
for _ in range(T):
    start, end = map(int,input().split())
    print(BFS(start, end))