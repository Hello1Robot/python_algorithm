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