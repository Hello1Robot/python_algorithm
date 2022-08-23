N = list(input())
nums = list(map(str, range(10)))
res = [] # 숫자 들어오면 넣을 리스트
stk = [] # 연산자 넣을 스택

# 오류가 발생할 수 있는 상황
# 1. 괄호 안닫히기
# 2. 0 나누기
# 3. 연산할 게 없는 경우

for n in N:
    if n in nums: # 숫자면 res에 넣기
        res.append(n)
    elif n == '(':
        stk.append(n)
    elif n == ')':
        while stk:
            x = stk.pop()
            if x == '(':
                break
            elif x == '*':
                if len(res) < 2:
                    print('ROCK')
                    exit()
                a = res.pop()
                b = res.pop()
                c = int(a)*int(b)
                res.append(str(c))
            elif x == '+':
                if len(res) < 2:
                    print('ROCK')
                    exit()
                a = res.pop()
                b = res.pop()
                c = int(a)+int(b)
                res.append(str(c))
            elif x == '-':
                if len(res) < 2:
                    print('ROCK')
                    exit() 
                a = res.pop()
                b = res.pop()

                c = int(a)-int(b)
                res.append(str(c))
            elif x == '/': 
                if len(res) < 2:
                    print('ROCK')
                    exit()
                a = res.pop()
                b = res.pop()
                if b == '0':
                    print('ROCK')
                    exit()
                c = int(a)//int(b)
                res.append(str(c))
    elif n == '+' or n == '-': # 연산자일 경우 스택을 확인. +의 경우 순위가 낮아서 다 수행해야됨
        while stk:
            if stk[-1] == '(':
                break
            else:
                x = stk.pop()
                if x == '+':  # 더하기 경우, 뒤에서 두개 뽑아서 계산하고 집어넣기
                    if len(res) < 2:
                        print('ROCK')
                        exit()
                    a = res.pop()
                    b = res.pop()
                    c = int(a)+int(b)
                    res.append(str(c))
                elif x == '*': # 곱하기도 뒤에서 두 개 뽑아서 계산하고 집어넣기
                    if len(res) < 2:
                        print('ROCK')
                        exit()
                    a = res.pop()
                    b = res.pop()
                    c = int(a)*int(b)
                    res.append(str(c))
                elif x == '-': 
                    if len(res) < 2:
                        print('ROCK')
                        exit()
                    a = res.pop()
                    b = res.pop()
                    c = int(a)-int(b)
                    res.append(str(c))
                elif x == '/': 
                    if len(res) < 2:
                        print('ROCK')
                        exit()
                    a = res.pop()
                    b = res.pop()
                    if b == '0':
                        print('ROCK')
                        exit()
                    c = int(a)//int(b)
                    res.append(str(c))                
        stk.append(n)
    elif n == '*': # 위와 동일.
        while stk:
            if stk[-1] == '+' or stk[-1] == '-' or stk[-1] == '(': # +보다는 순위가 높으니까 +는 통과
                break
            elif stk[-1] == '*':
                if len(res) < 2:
                    print('ROCK')
                    exit()
                stk.pop()
                a = res.pop()
                b = res.pop()
                c = int(a)*int(b)
                res.append(str(c))
            elif stk[-1] == '/':
                if len(res) < 2:
                    print('ROCK')
                    exit()
                stk.pop()
                a = res.pop()
                b = res.pop()
                if b == '0':
                    print('ROCK')
                    exit()
                c = int(a)//int(b)
                res.append(str(c))  
        stk.append(n)
                                          
while stk: # 남은 스택이 없을 때까지 계산반복
    x = stk.pop()
    if x == '+':
        if len(res) < 2:
            print('ROCK')
            exit()
        a = res.pop()
        b = res.pop()
        c = int(a)+int(b)
        res.append(str(c))
    elif x == '*':
        if len(res) < 2:
            print('ROCK')
            exit()
        a = res.pop()
        b = res.pop()
        c = int(a)*int(b)
        res.append(str(c))
    elif x == '-': 
        if len(res) < 2:
            print('ROCK')
            exit()
        a = res.pop()
        b = res.pop()
        c = int(a)-int(b)
        res.append(str(c))
    elif x == '/': 
        if len(res) < 2:
            print('ROCK')
            exit()
        a = res.pop()
        b = res.pop()
        if b == '0':
            print('ROCK')
            exit()
        c = int(a)//int(b)
        res.append(str(c))  
if len(res) != 1:
    print('ROCK')
else:
    print(res[0])