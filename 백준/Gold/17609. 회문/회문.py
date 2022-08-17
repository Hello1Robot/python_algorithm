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
# 다른 반례들 다 해결할 수 있도록 구성은 했는데
# aabcbcaa 어떻게? - 해결
# 다음 반례 : xyxcxyxy
N = int(input())
for _ in range(N):
    pldr = input()
    res_cnt = 0
    i = 0
    j = len(pldr)-1
    while i <= j:
        if pldr[i] == pldr[j]:
            i += 1
            j -= 1
        else:
            case1 = pldr[i+1:j+1]
            case2 = pldr[i:j]
            if case1 == case1[::-1] or case2 == case2[::-1]:
                res_cnt = 1
                break
            else:
                res_cnt = 2
                break


    print(res_cnt)