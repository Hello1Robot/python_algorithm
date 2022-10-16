# 대충 함수만들어서 어캐어캐 해보자
# 일단 조건부터 받아적기
# 생각은 재귀함수를 돌림
# 숫자의 범위는 M-N+1만큼만.
# 이러면 뭐 1 1 1 1 1 1
# 1 1 1 1 1 2
# 대충 이따위로 나올듯.
# 그럼 함수의 구성 생각
# 고른 숫자의 수를 적는 카운트 n
# 현재까지 고른 숫자의 합을 적어놓는 m
# 출력할 str을 넣어둘 st
# 셋 만 있어도 될듯? 나머지는 글로벌값으로.
# 아니다. 비내림차순으로 만들어야 한다
# 그렇기 때문에 이전에 선택한 값을 저장할 pre 하나 만듦
# 그이외에 글로벌카운트 cnt하나 만들기
# 아~ 백트래킹 다 했는데 왜 시간초과냐구~~
# 근데 터질만했음ㄹㅇㅋㅋ
# 재귀라 더그런듯?

# 재귀돌리면서 범위를 수정해야 됨
# nums를 만드는 게 아니었음! 
# 아니 아예 안도는거 너무 섭섭한데?!
# bfs로 돌아가기
from collections import deque

# def dfs(n, m, st, pre):
#     global cnt
#     if m > M:
#         return
#     elif n == N:
#         if m == M:
#             cnt += 1
#             if cnt == K:
#                 print(st.strip())
#                 exit()
#     else:
#         for x in range(1,M-(N-n)-m+2):
#             if x >= pre:
#                 dfs(n+1, m+x, st+' '+str(x), x)

def bfs(N, M, K):
    que = []
    que.append((0, 0, '', 0))
    cnt = 0
    while que:
        n, m, st, pre = que.pop()
        if m > M:
            continue
        if n == N:
            if m == M:
                print(st.strip())
                cnt += 1
                if cnt == K:
                    print(st.strip())
                    return
        for x in range(1,M-(N-n)-m+2):
            if x >= pre:
                que.append((n+1, m+x, st+' '+str(x), x))

            
N, M, K = map(int,input().split()) # N개의 숫자를 뽑아서 값의 합이 M인 K번째 경우를 출력하기
cnt = 0
# dfs(0,0,'',0)
bfs(N, M, K)