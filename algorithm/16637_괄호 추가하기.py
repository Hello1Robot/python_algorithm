# 이건 양수일 때만.
# 음수가 될 경우는 최대한 빨리 곱해야됨...
N = int(input())
qst = tuple(input())
stk = [int(qst[0])]
opers = ['+','-','*']
for i in range(1,N):
    if qst[i] in opers:
        stk.append(qst[i])
    else:
        if stk[-1] == '+':
            stk.pop()
            stk[-1] += int(qst[i])
        elif stk[-1] == '*':
            stk.append(int(qst[i]))
        else:
            stk.pop()
            now = 1
            while stk:
                num = stk.pop()
                if num != '*':
                    now *= num
            stk.append(now-int(qst[i]))

now = 1
while stk:
    num = stk.pop()
    if num != '*':
        now *= num
print(now)
