N = int(input())
total = 0
cnt = 0
if N < 10:
    print(0)
    if N % 3 !=0:
        print('NO')
    else:
        print('YES')
while(N>9):
    for i in str(N):
        total = total + int(i)
    if total < 10:
        cnt += 1
        print(cnt)
        if total % 3 != 0:
            print("NO")
        else:
            print("YES")
        break
    else:
        cnt+= 1
        N = total
        total = 0
        continue

