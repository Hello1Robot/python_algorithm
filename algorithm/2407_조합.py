# 조합 공식은 n! / (n-r)! r!
# n, r이 주어졌을 때 일단 (n-r)을 구한다.
n, r = map(int,input().split())
if n == r:
    print(1)
    exit()
m = n-r
if m < (n-m):
    m = (n-m)

분모 = 1
for i in range(n,m,-1):
    분모 *= i

분자 = 1
for j in range(1,r+1):
    분자 *= j

print(분모//분자)