# 브루트포스적으로 접근
# 두 번 이상 시킨 메뉴들 모아서
# 하나의 리스트에 담아 두고
# 해당 리스트에 있는 것들로 2부터 최대N까지 순열만들어서
# 2명 이상이 주문한 메뉴 조합을 후보에 넣는다.
# 맥스랑 같을 경우에도 집어넣는다.

from itertools import combinations


def solution(orders, course):
    answer = []
    orders.sort(key=lambda x : len(x))

    for i in course:
        max_cnt = 1
        res = []
        for j in range(len(orders)):
            for com in combinations(orders[j], i):
                cnt = 0
                for k in range(j,len(orders)):
                    for c in com:
                        if c not in orders[k]:
                            break
                    else:
                        cnt += 1
                if cnt > max_cnt:
                    max_cnt = cnt
                    res.clear()
                    res.append(''.join(com))
                elif cnt == max_cnt:
                    res.append(''.join(com))
        answer.extend(res)

    answer.sort()


    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
