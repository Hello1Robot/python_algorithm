N = list(input())
stk = [] # 스택

for n in N:
    if n.isalpha():
        print(n, end='') # 문자 출력
    elif n == '(':
        stk.append(n)
    elif n == '-' or n =='+': # -나 +의 경우(순위낮음)
        while stk:
            if stk[-1] == '(': # ( 만나면 탈출
                break
            else: # 그 이외에는 순위가 높은 게 없으니까, 다 빼내기
                print(stk.pop(), end='')
        stk.append(n) # 다 빼낸 후 스택에 넣기
    elif n == '*' or n == '/': # 곱하기나 나누기의 경우
        # 더하기나 빼기보다 순위가 높기 때문에, 그 이전까지만 빼내기
        while stk:
            if stk[-1] == '(':
                break
            elif stk[-1] == '-' or stk[-1] == '+':
                break
            else:
                print(stk.pop(), end='')
        stk.append(n) # 빼낸 이후 스택에 넣기
    elif n == ')': # 닫는 괄호가 왔을 때는, ( 가 나올 때 까지 다빼기
        while stk:
            if stk[-1] == '(':
                stk.pop()
                break
            else:
                print(stk.pop(), end='')
while stk: # 스택 남은 거 빼내기
    print(stk.pop(), end='')
print()