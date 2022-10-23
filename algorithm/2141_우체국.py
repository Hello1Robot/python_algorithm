# 가운데 지으면 되나?
# 가운데 위치를 어캐 찾지?
# 일직선 쭉 늘어놓기
# 예시 생각해보면 (1,3) (2,5) (3,3)
# 그럼 11122222333 아닌가
import sys
input = sys.stdin.readline
N = int(input())
viliges = []
row = ''
for _ in range(N):
    a, b = map(int,input().split())
    viliges.append((str(a), b))
viliges.sort()
for a, b in viliges:
        row = row + a*b
print(row)
print(row[len(row)//2])

# 메 모 리 초 과 아