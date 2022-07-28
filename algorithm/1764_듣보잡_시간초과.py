import sys

N, M = map(int, input().split())

D = tuple(sys.stdin.readline().strip() for _ in range(N))

DBJ = []

for i in range(M):
    B = sys.stdin.readline().strip()
    if B in D:
        DBJ.append(B)

DBJ.sort()
print(len(DBJ))

for i in DBJ:
    print(i)

# 중복되면 이름을 빼고 DBJ리스트에 넣어야 함.
# DBJ리스트는 사전순으로 정렬.
# DBJ의 len을 표시

# 근데 굳이 듣 + 보를 다른 데 모아야할까?
# 이것도 어제 했던 것처럼 두 개가 되면 하나를 DBJ에 넣는걸로
# 하면 되지 않을까?
# 같은 값이 있으면 오류가 나는 게 set인가? 아닌데

