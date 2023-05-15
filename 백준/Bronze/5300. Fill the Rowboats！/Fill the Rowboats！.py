N = int(input())
for i in range(1,N+1):
    print(i, end=" ")
    if not i%6 or i == N:
        print("Go!", end=" ")