# 세금 책정
# G1, G2로 분할
# G1에는 C%의 세금
# G2에는 세금 X
# 총합한 뒤, G2의 제곱 * D 만큼의 세금
# 기본적으로 브루트포스같은 문제인듯
# C는 세금, n이랑 a는 안쓸 듯
# d는 퍼센트고
# 그룹2의 최대값 제곱에다가 한 게 어쩌구.
# 그럼 두 부분으로 나누기 위해서 함수를 짜야 함

from itertools import combinations
from collections import defaultdict


# # 갯수가 n으로 주어짐
# b = [1,3,100,200]
# for i in range(4):
#     x = list(combinations(range(4), i))

#     for xx in x:
#         yy = [y for y in range(4) if y not in xx]
#         print(xx)
#         print(yy)


# 같은 시청자가 도네이션을 여러 번 할 수 있는데
# 이럴 경우에는 시청ㅈ 하나를 뭉탱이로 해야 함
n = 2
c = 1
d = 10000
a = ["fan","Fan"]
b = [1,2]
answer = 0

donation_list = defaultdict(int)

for i in range(n):
    donation_list[a[i]] += b[i]

donations = list(donation_list.values())
nums = len(donations)

for i in range(nums+1):
    g1_list = combinations(range(nums), i)
    for g1 in g1_list:
        g2 = [x for x in range(nums) if x not in g1]
        tot_g1 = 0
        tot_g2 = 0
        g2_list = []
        for gg1 in g1:
            tot_g1 += donations[gg1]
        
        tex_g1 = (tot_g1 / 100) * (100-c)
        
        for gg2 in g2:
            g2_list.append(donations[gg2])
            tot_g2 += donations[gg2]

        if tot_g2:
            result = ((tex_g1 + tot_g2) - (d/100 * (max(g2_list)**2))) * 100
        else:
            result = tex_g1 * 100
        
        answer = max(answer, result)

print(answer)

