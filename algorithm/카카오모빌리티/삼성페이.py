# 페이 10% 할인쿠폰
# 하루 최대 1장 고객당 최대 k장
# 쿠폰 몇 개 나누어졌는지 리턴
# 문자열 다룰 수 있는지 확인하는 문제
# k번 사는 거 카운트해서, k번까지 꽉 찼으면 카운트 더 안하기 해야될 듯

# 문자열로 나오니까, 꺼내면서 리스트화시켜줌
# 하루 한 번의 제한을 확인해야 할듯.
# 효율성 고려 안하면 쉽게 할 수 있는 문제긴 함
def solution(id_list, k):
    answer = 0
    id_dict = {}
    for idss in id_list:
        ids = idss.split(' ')
        todayBuyers = []
        for id in ids:
            if id not in id_dict:
                id_dict[id] = 1
                answer += 1
                todayBuyers.append(id)
            else:
                if id_dict[id] == k:
                    continue
                elif id not in todayBuyers:
                    id_dict[id] += 1
                    todayBuyers.append(id)
                    answer += 1


    return answer

print(solution(["JAY", "JAY ELLE JAY MAY", "MAY ELLE MAY", "ELLE MAY", "ELLE ELLE ELLE", "MAY"], 3))