# 스트링으로 만들어서 가운데 찾는 건
# 아마 길이가 길어져서 펑 터지는게 아닌가 싶음
# 딕셔너리를 만들어서 서치?
# 이전 코드에서도 어차피 받고 소트해야 해서 두 번의 과정이 필요했는데
# 그러면서 사람 수 세서 토탈 인구 구해
# 토탈 절반값이 목표
# 순회하면서 인구수만큼 카운트 더해주고, 만약 카운트가 토탈 절반값보다 커지면 펑
import sys
input = sys.stdin.readline

N = int(input())
vilages = []
tot = 0
cnt = 0
for _ in range(N):
    a, b = map(int,input().split())
    tot += b
    vilages.append((a,b))
vilages.sort()
# 짝수면 절반 때리면 되는데 홀수면 +1해줘야함
center = 0
if tot%2:
    center = tot//2 + 1
else:
    center = tot//2

for a, b in vilages:
    cnt += b
    if cnt >= center:
        print(a)
        break