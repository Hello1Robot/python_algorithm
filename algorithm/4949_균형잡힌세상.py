while True:
    N = input()
    if N == '.':
        break
    else:
        ea = {'(':0, ')':0, '[':0, ']':0}
        for i in N:
            if i in ea.keys():
                ea[i] += 1

        if ea['('] == ea[')'] and ea['['] == ea[']']:
            print('yes')
        else:
            print('no')
# 순서를 생각해야되는데
 
# 만약 [ ( ] ) 인 경우가 있으면

# 이를 어떻게 걸러낼것인지에 대한 아이디어가 필요함.
