N = int(input())
for _ in range(N):
    ss = input()
    print(ss[0], end = "")
    for i in range(1,len(ss)):
        if ss[i] != ss[i-1]:
            print(ss[i], end = "")
    print()
        