# 전체 경우의 수를 다 탐색해보는 코드를 작성해봐야 할 듯
# 각 점수에 따라 두 가지 선택 : 어피치쉑 갯수 +1 쏘던가 안쏘던가 = n+1 or 0
# 그럼 비트연산자 아니냐구... 근데 숙련이 안되서 못쓰겠어...


max_score = 1
def solution(n, info):

    def f(i,N,c,a):
        global max_score
        if i == 11:
            bit[10] = N-c
            score = 0
            vic = 0
            for i in range(11):
                if bit[i] > info[i]:
                    score += (10-i)
                if bit[i] <= info[i] and info[i]:
                    vic += (10-i)
            if score-vic >= max_score:
                max_score = score-vic
                print(bit)
                answer = bit[:]
            

        else:
            if N >= c+info[i]+1:
                bit[i] = info[i]+1
                f(i+1,N,c+(info[i]+1),a)
            bit[i] = 0
            f(i+1,N,c,a)


    bit = [0] * 11
    answer = []
    f(0,n,0,answer)
    if len(answer) == 0:
        answer = [-1]
        
    return answer


# print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))
# print(solution(1, [1,0,0,0,0,0,0,0,0,0,0]))
print(solution(9, [0,0,1,2,0,1,1,1,1,1,1]))