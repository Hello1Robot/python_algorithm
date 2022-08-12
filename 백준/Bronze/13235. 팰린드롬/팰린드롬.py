st = list(input())
res = True
for i in range(len(st)//2):
    if st[i] != st[len(st)-1-i]:
        res = False
        break

if res:
    print('true')
else:
    print('false')