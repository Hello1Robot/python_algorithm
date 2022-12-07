from collections import deque
A = input() # A값 받아오기.
B = deque(input()) # B값 받아오기. pop과 popleft를 사용할 예정이므로 deque로 만들기
reverse_flag = 0 # 뒤집혔는지 아닌지를 판별하는 변수 선언

while len(B)> len(A): # B의 길이가 A의 길이와 같아질 때까지 반복
    if reverse_flag: # 만약 뒤집혀있으면
        if B[0] == 'A': # 첫번째 변수를 확인함
            B.popleft()
        else:
            B.popleft()
            reverse_flag = 0
    else: # 만약 뒤집히지 않았으면
        if B[-1] == 'A': # 마지막 변수를 확인함
            B.pop()
        else:
            B.pop()
            reverse_flag = 1

res_B = ''.join(B) # 비교를 위해서 B를 문자열로 만듦
if reverse_flag: # 만약 뒤집혀있을 경우에는
    if res_B[::-1] == A: # B를 뒤집어서 비교
        print(1)
    else:
        print(0)
else:
    if res_B == A:
        print(1)
    else:
        print(0)