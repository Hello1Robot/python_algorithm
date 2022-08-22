import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 잘라나가다가, M보다 작아지면 그 이전 값을 출력하자
woods = list(map(int, input().split()))
cut = max(woods)
tot = 0
while tot < M:
    tot = 0
    for wood in woods:
        if cut <= wood:
            tot += wood-cut
    cut -= 1

print(cut+1)