# 백 트 래 킹
# 기본적으로 상하좌우대각선 고려해서 퀸 놓을 때마다 상하죄우대각선 전부 1로 변경하고 0인 곳 중에서 다시 탐색하는데,
# 이거 재귀로 구현하는 건 어떨까싶은데
# 방문처리 하고 / 풀어주고 두 가지 경우로 해서
# 계속 들어가게 하면 될 거 같은데?
def 퀸찾기(n):
    global 가로, 아래대각, 위대각
    global cnt
    if n==N:
        cnt += 1
        return

    for i in range(N):

        if 가로[i] and 아래대각[n+i] and 위대각[n-i+N-1]:

            가로[i] = False
            아래대각[n+i] = False
            위대각[n-i+N-1] = False

            퀸찾기(n+1)

            가로[i] = True
            아래대각[n+i] = True
            위대각[n-i+N-1] = True

cnt = 0

N = int(input())


가로 = [True]*N
아래대각 = [True]*(2*N-1)
위대각 = [True]*(2*N-1)



퀸찾기(0)

print(cnt)