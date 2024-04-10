n = list(input())
flag = 1
for i in range(len(n)//2):
    if n[i] != n[len(n)-i-1]:
        flag = 0
        break

print(flag)