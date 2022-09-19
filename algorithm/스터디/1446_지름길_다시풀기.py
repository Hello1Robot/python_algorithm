import sys
input = sys.stdin.readline

N, D = map(int,input().split())
지름길들 = []
DP = list(range(D+1))

for _ in range(N):
    시작점, 도착점, 비용 = map(int,input().split())
    if (도착점-시작점) < 비용 or 도착점 > D:
        continue
    else:
        지름길들.append((도착점, 시작점, 비용))
지름길들.sort() # 뒤집기

for 도착점, 시작점, 비용 in 지름길들:
    비교 = DP[시작점]+비용

    if DP[D] > 비교:
        cnt = 0
        for i in range(도착점, D+1):
            DP[i] = 비교 + cnt
            cnt += 1

print(DP[D])
