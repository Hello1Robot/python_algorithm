T = int(input())
for test_case in range(T):
    N = int(input())
    res = '0'
    st_list = [input() for _ in range(N)]
    for i in range(len(st_list)):
        for j in range(len(st_list)):
            if i != j:
                A = st_list[i] + st_list[j]
                x = A[0:(len(A)//2)]
                x2 = A[::-1]
                x2 = x2[0:(len(A)//2)]
                if x==x2:
                    res = A
                    break
    print(res)