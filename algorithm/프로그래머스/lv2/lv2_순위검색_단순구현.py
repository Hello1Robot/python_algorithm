# 시간초과나~
# 어떡해~

def solution(info, query):
    answer = []

    for que in query: # 쿼리는 8개의 단어로 되어있음
        a1, _, b1, _, c1, _, d1, e1 = que.split()
        cnt = 0
        for st in info:
            a2, b2, c2, d2, e2 = st.split()
            if (a2 == a1 or a1 == '-') and (b2 == b1 or b1 == '-') and (c2 == c1 or c1 == '-') and (d2 == d1 or d1 =='-'):

                if int(e2) >= int(e1):
                    cnt += 1

        answer.append(cnt)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))