T = int(input())
for _ in range(T):
    eq = list(input())
    stk = []
    res = 'YES'
    for q in eq:
        if q == '(':
            stk.append(q)
        elif q == ')':
            if not stk:
                res = 'NO'
            else:
                stk.pop()
    if stk:
        res = 'NO'
    print(res)