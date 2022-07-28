T = int(input())

for test_case in range(1,T+1):
    A, B = map(int, input().split())
    C = 0
    res = 0
    Q = A % 10
    if Q == 0:
        res = 10
    elif Q in [1, 5, 6]:
        res = Q
    elif Q in [3, 7, 8] :
        
    elif Q in [4,9]    

