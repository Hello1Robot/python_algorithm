import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = map(int,input().split())
    if A == 1 or B == 1:
        print(10)
        continue
    A_list = []
    while A:
        A_list.append(A)
        A = A // 2

    while B:
        if B in A_list:
            print(B*10)
            break
        B = B // 2

