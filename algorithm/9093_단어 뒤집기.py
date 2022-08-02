T = int(input())

for case in range(1, T+1):
    N = input().split()

    for i in N:
        print(i[::-1], end=' ')
    print()
        
        