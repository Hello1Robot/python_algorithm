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