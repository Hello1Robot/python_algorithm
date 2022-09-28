# 아이디어 전개
# 숫자로 바꿔서 서칭하기
# 조건이 총 5개
# 언어, 직군, 경력, 소울푸드, 점수
# 언어는 3가지, 직군은 2가지, 경력은 2가지, 소울푸드는 2가지 가 나옴
# 각 속성을 숫자로 바꾸는 게 어떨까
# cpp = 1000000 java = 2000000 python = 3000000
# backend = 100000 frontend = 200000
# junior = 10000 senior = 20000
# chicken = 1000 pizza = 2000 
# 이런 식으로 만들면 java backend junior chichen 150점 = 2111150 이 나옴

# 이러면 한번 만들어놓고 빼기연산으로 처리할 수 있음 (일반적인 쿼리의 경우만)
# '-'의 경우엔 어떻게 해야 될 지 무릎꿇고 고민함


def solution(info, query):
    answer = []
    info_nums = []
    for st in info:
        num = 0
        a, b, c, d, e = st.split()
        if a == "java":
            num += 9000000
        elif a == "cpp":
            num += 8000000
        elif a == "python":
            num += 7000000
        
        if b == "backend":
            num += 900000
        else:
            num += 800000
        
        if c == 'junior':
            num += 90000
        else:
            num += 80000
        
        if d == 'chicken':
            num += 9000
        else:
            num += 8000
        num += int(e)
        info_nums.append(num)
    
    for que in query: # 쿼리는 8개의 단어로 되어있음
        a, _, b, _, c, _, d, e = que.split()
        cnt = 0
        if a == "java":
            num += 9000000
        elif a == "cpp":
            num += 8000000
        elif a == "python":
            num += 7000000
        elif a == '-':
            num += 4000000
        
        if b == "backend":
            num += 900000
        elif b == "frontend":
            num += 800000
        elif b == '-':
            num += 400000
        
        if c == 'junior':
            num += 90000
        elif c == 'senior':
            num += 80000
        elif c == '-':
            num += 40000

        
        if d == 'chicken':
            num += 9000
        elif d == 'pizza':
            num += 8000
        elif d == '-':
            num += 4000
        num += int(e)
        for num2 in info_nums:
            res = num2 - num
            if res <= 0:
                continue
            if res < 1000:
                cnt += 1
            


    return answer




info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))