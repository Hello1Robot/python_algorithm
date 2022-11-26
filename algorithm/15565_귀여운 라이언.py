# 투포인터
# 사실 뭔지 모르겠음
# 1과 2가 주어지는데
# 1의 갯수와 2의 갯수를 세 놓는 게 좋을까?
# 근데 1의 갯수를 세려면 어차피 1번 순회해야 되지 않나
# 1000000개를 한번 돌아야되네

from sys import stdin; input=stdin.readline

N, K = map(int,input().split())
dolls = tuple(map(int,input().split()))
total_ryan = dolls.count(1)
if total_ryan < K:
    print(-1)
    exit()
if K == 1:
    print(1)
    exit()
sp = 0
ep = N-1
# 시작점 찾기
for i in range(N):
    if dolls[i] == 1:
        sp = i
        break

# 끝점 찾기
for j in range(N-1,-1,-1):
    if dolls[j] == 1:
        ep = j
        break

if total_ryan == K:
    print(j-i)
    exit()

pre_start = sp
pre_end = ep
while sp < ep:
    sp += 1
    if dolls[sp] == 1:
        total_ryan -= 1
        pre_start = sp
        ep = pre_end

    if total_ryan == K:
        print(pre_end-pre_start)
        exit()
    ep -= 1
    if dolls[ep] == 1:
        total_ryan -= 1
        pre_end = ep
        sp = pre_start
    if total_ryan == K:
        print(pre_end-pre_start)
        exit()

print(-1)

    
