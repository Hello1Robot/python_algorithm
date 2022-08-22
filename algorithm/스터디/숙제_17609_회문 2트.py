# 회문이면 0, 유사회문이면 1, 둘 다 아니면 2를 출력
# 한 문자를 '삭제하면' 회문이 되는 것 = 유사회문
# 투포인터를 생각하면서 문제 풀이
# i와 j를 움직이면서 경우의 수 생각하기
# 만약 i와 j가 같으면 그냥 움직이기
# 다를경우 i와 j-1, i+1과 j를 비교함
# 만약 위에 둘 중 하나가 같다면
# 결과카운터를 하나 올리고, i나 j 값을 수정함
# 만약 둘 다 같지 않다면 : 결과카운터 2. break
# 만약 둘 다 같으면? 예시를 생각해보자
# abcccccab 의 경우? - 둘 중 하나만 없애도 됨. aba or bab
# 그럴 경우, 다음 것까지 비교해보는 게 좋을듯? 흠
N = int(input())
for _ in range(N):
    pldr = list(input())
    res_cnt = 0
    i = 0
    j = len(pldr)-1
    while i <= j:
        if pldr[i] == pldr[j]:
            i += 1
            j -= 1
        else:
            if pldr[i] == pldr[j-1] and pldr[i+1] == pldr[j]:
                if pldr[i+2] == pldr[j-3]:
                    i += 1
                    j -= 2
                    res_cnt += 1
                elif pldr[i+3] == pldr[j-2]:
                    i += 2
                    j -= 1
                    res_cnt += 1
                else:res_cnt += 2
            elif pldr[i] == pldr[j-1]:
                res_cnt += 1
                i += 1
                j -= 2
            elif pldr[i+1] == pldr[j]:
                res_cnt += 1
                i += 2
                j -= 1
            else:
                res_cnt += 2
                break
        if res_cnt >= 2:
            res_cnt = 2
            break

    print(res_cnt)