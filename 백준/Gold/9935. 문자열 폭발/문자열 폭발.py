# 대충 아이디어
# 문자열 스택에 넣으면서 순회하기
# 넣다가 m[0]과 동일하면 x+1 계속 해주기.
# 만약 x가 m의 길이에 도달하면 펑!
# 나머지 순회하고, 터졌으니까 그걸 다시 순회
import sys
N = list(sys.stdin.readline().strip())
M = list(sys.stdin.readline().strip())
boom = len(M)
stk = []
flag = 0

for x in range(len(N)):
    stk.append(N[x])
    if N[x] == M[-1]:
        if stk[-boom:] == M:
            for _ in range(boom):
                stk.pop()
        


if stk:
    for n in stk:
        print(n, end='')
else:
    print('FRULA')
