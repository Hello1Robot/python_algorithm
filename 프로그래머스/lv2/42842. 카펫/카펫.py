# 수학적으로 접근하면 될 듯한 문제
# 아닌가?! 내가 보기엔 좀 수학적임
# 2 = 2,1 흠...
# 어차피 전체 크기는 나오잖아? 브라운 + 옐로우
# 옐로우 조합 짜서 어쩌구저쩌구 하면 될 듯.


def solution(brown, yellow):
    answer = []
    for i in range(1,yellow+1):
        if not yellow % i:
            a = yellow // i
            if (a+2)*(i+2) == (brown+yellow):
                answer.append(max(a+2,i+2))
                answer.append(min(a+2,i+2))
                break
    
    return answer