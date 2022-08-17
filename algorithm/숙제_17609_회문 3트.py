# 메 모 리 초 과

# 1번과 2번을 합친 방법
# while로 투 포인터로 양 끝에서 전진하고
# 혹시 맞지 않는 게 나오면 삭제할 대상을 설정
# 삭제한 이후 회문검사를 통해 0인지 2인지 확인

N = int(input())
for _ in range(N):
    st = input()
    i = 0 # 시작점
    j = len(st)-1 # 끝점
    check_list = []
    res_cnt = 0
    if st == st[::-1]:
        print(0)
        break
    else:
        while i <= j:
            if st[i] != st[j]:
                res_cnt = 1
                if st[i] == st[j-1] and st[i+1] == st[j]:
                    res1 = st[:i] + st[i+1:]
                    res2 = st[:j] + st[j+1:]

                    check_list.append(res1)
                    check_list.append(res2)
                elif st[i] == st[j-1]:
                    res = st[:j] + st[j+1:]
                    check_list.append(res)
                elif st[j] == st[i+1]:
                    res = st[:i] + st[i+1:]
                    check_list.append(res)
                else:
                    res_cnt = 2
            if res_cnt > 1:
                break
            else:
                i += 1
                j -= 1
        
        if res_cnt == 1:
            for res in check_list:
                if res == res[::-1]:
                    res_cnt = 1
                    break
                else:
                    res_cnt = 2
        elif res_cnt > 1:
            res_cnt = 2
        
        print(res_cnt)
