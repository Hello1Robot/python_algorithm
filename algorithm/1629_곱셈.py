A, B, C = map(int,input().split())

res = 1
for i in range(B):
    res = (A**2)%C

print(res)