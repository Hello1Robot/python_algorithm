from collections import deque
A = input()
B = deque(input())

reverse_flag = 0
while len(B)> len(A):
    if reverse_flag:
        if B[0] == 'A':
            B.popleft()
        else:
            B.popleft()
            reverse_flag = 0
    else:
        if B[-1] == 'A':
            B.pop()
        else:
            B.pop()
            reverse_flag = 1

res_B = ''.join(B)
if reverse_flag:
    if res_B[::-1] == A:
        print(1)
    else:
        print(0)
else:
    if res_B == A:
        print(1)
    else:
        print(0)