# 주어진 명령을 순서대로 구현하는 문제
# 각 명령을 모듈화해도 되고, 절차화해도 된다고 생각
# 파이썬의 경우 관련된 함수가 많으므로, 절차적으로 푸는 게 나쁘지 않을 듯.
# 문제의 형식이 백준보다는 다른 곳에 많이 나오는 느낌

# 알파벳 대문자와 소문자는 구별하지 않는다.
# 공백이 하나 이상이라면, 공백의 크기는 관계없다. 물론 어떤 문자열엔 공백이 있고 어떤 문자열엔 공백이 없는 것, 즉 공백 유무의 차이 자체는 문제가 된다.
# 문자열의 맨 앞 혹은 맨 뒤에 나타나는 공백은 있으나 없으나 관계없다.
# 특수 부호의 바로 앞이나 바로 뒤에 나오는 공백도 있으나 없으나 상관없다.
# 여는 괄호끼리는 종류를 구별하지 않는다.
# 닫는 괄호끼리는 종류를 구별하지 않는다.
# 쉼표(",")와 세미콜론(";")은 구별하지 않는다.

from sys import stdin; input = stdin.readline

check_list = ["(", ")", "[", "]", "{", "}", ".", ",", ";", ":"]

N = int(input())

# def check_sentence(st):
#     new_st = ""
#     for i in range(len(st)):
#         if st[i] == ";":
#             new_st += ","
#         elif st[i] == "{" or st[i] ==  "[":
#             new_st += "("
#         elif st[i] == "}" or st[i] ==  "]":
#             new_st += ")"
#         elif st[i] == " ":
#             if st[i-1] != " " and st[i-1] not in check_list and st[i+1] not in check_list:
#                 new_st += " "
#         else:
#             new_st += st[i]
            
#     return new_st
        
def check_sentence(s):
    s = s.strip().replace(',', ';').lower()
    for c in "{[": s = s.replace(c, '(')
    for c in "}]": s = s.replace(c, ')')
    while '  ' in s: s = s.replace('  ', ' ')
    for c in "().,;:": s = s.replace(' '+c, c).replace(c+' ',c)
    return s

for t in range(1,N+1):
    sen1 = input().strip()
    sen2 = input().strip()
    filterA = check_sentence(sen1)
    filterB = check_sentence(sen2)
    print(f"Data Set {t}: {'not ' if filterA != filterB else ''}equal")
    print()
