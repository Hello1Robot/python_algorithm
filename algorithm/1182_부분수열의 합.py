import sys
input = sys.stdin.readline

def f(i,N,a,G):
    global cnt
    if i == N:
        if a == G:
            cnt += 1
    else:
        bit[i] = A[i]
        f(i+1,N,a+A[i],G)
        bit[i] = 0
        f(i+1,N,a,G)

N, G = map(int,input().split())
cnt = 0
A = list(map(int,input().split()))
bit = [0]*N
f(0,N,0,G)
if G == 0:
    cnt -= 1
print(cnt)
