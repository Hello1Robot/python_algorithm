str_list = input().split()
res = []
# 몇 가지 예시를 생각해보자
# <ab cd> 의 경우.
# <open>tag<close> 의 경우
# <int><max>2147483647<long long><max>
# 합치는게 맞을까, 아니면 스트링으로 처리하는 게 나을까
# < > 사이의 단어는 돌리지 않기
# > < 는 돌리기
# 끊어서 저장하는 게 더 편하긴 할듯.
for st in str_list:
    for s in st:
        