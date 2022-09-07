T = int(input())
for _ in range(T):
    N = int(input())

    cloth_dict = {}
    for i in range(N):
        l, wear = input().split()
        if wear in cloth_dict:
            cloth_dict[wear] += 1
        else:
            cloth_dict[wear] = 1
    # 부분집합의 수 : (2*n)-1 #공집합을 뺌
    val_list = list(cloth_dict.values())
    res = (2**len(val_list))-1
    for val in val_list:
        res *= val
    
    print(res)
    
