def f(i, N):
    if i == N:
        a = sum(bit)
        if a == 100:
            if bit.count(0) == 2:
                bit.sort()
                for b in bit:
                    if b != 0:
                        print(b)
                exit()
            
    else:
        bit[i] = A[i] # 포함여부만을 bit에 나타냄
        f(i+1, N)
        bit[i] = 0
        f(i+1,N)

A = []
bit = [0]*9
for _ in range(9):
    A.append(int(input()))

f(0,9)