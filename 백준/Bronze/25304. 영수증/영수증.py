tot = int(input())
N = int(input())
비교 = 0
for i in range(N):
    a, b = map(int,input().split())
    비교 += a*b

if 비교 == tot:
    print('Yes')
else:
    print('No')