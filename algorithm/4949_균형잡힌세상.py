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
