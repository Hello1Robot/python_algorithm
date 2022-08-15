while True:
    N = input()
    if N == '0':
        break

    ans_cnt = 'yes'
    rst = list(N)
    if len(rst) % 2:
        rst.pop(len(rst)//2)
    for i in range(len(rst)//2):
        if rst[i] != rst[-1-i]:
            ans_cnt = 'no'
            break
    print(ans_cnt)