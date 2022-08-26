# 별은 4, 동그라미는 3, 네모는 2, 세모는 1
T = int(input())
for _ in range(T):
    a_dict = {'4':0, '3':0, '2':0, '1':0}
    b_dict = {'4':0, '3':0, '2':0, '1':0}
    alen, *az = input().split()
    blen, *bz = input().split()
    for a in az:
        a_dict[a] += 1
    
    for b in bz:
        b_dict[b] += 1
    
    a_val = list(a_dict.values())
    b_val = list(b_dict.values())
    if a_val[0] > b_val[0]:
        print('A')
    elif a_val[0] < b_val[0]:
        print('B')
    else:
        if a_val[1] > b_val[1]:
            print('A')
        elif a_val[1] < b_val[1]:
            print('B')
        else:
            if a_val[2] > b_val[2]:
                print('A')
            elif a_val[2] < b_val[2]:
                print('B')
            else:
                if a_val[3] > b_val[3]:
                    print('A')
                elif a_val[3] < b_val[3]:
                    print('B')
                else:
                    print('D')