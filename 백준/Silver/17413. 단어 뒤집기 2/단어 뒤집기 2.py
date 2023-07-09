# 문자열을 뒤집는데,
# 꺾새 사이에 있는 건 뒤집지 않아야 함
# 스택을 사용하면 될 듯??
# 문제가 정직하기 때문에 여는 것과 닫는 것이 무조건 세트로 등장함
# 리스트를 두 개 만들고, 순회하면서 넣으면 될 듯
# 띄어쓰기 만나면 초기화


quest = input()

stk = []
result = []
flag = False
for x in quest:
    if x == '<':
        while stk:
            a = stk.pop()
            result.append(a)
        result.append(x)
        flag = True
    elif x == '>':
        result.append(x)
        flag = False
    elif flag:
        result.append(x)
    else:
        if x == ' ':
            while stk:
                a = stk.pop()
                result.append(a)
            result.append(x)
        else:
            stk.append(x)

if stk:
    stk.reverse()
    result += stk

answer = ''.join(i for i in result)
print(answer)