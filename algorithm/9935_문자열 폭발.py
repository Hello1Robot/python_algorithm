N = list(input())
M = list(input())
cnt = 0
while True:
    newN = N.replace(M, '')
    if newN == N:
        break
    else:
        N = newN
if len(N):
    print(N)
else:
    print('FRULA')
    