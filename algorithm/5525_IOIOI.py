# 오랜만에 푸는 문 자 열 문제~
# 주어지는 N을 통해서 서치할 문자열을 만들고
# 그걸 통해서 주어지는 문자열에서 서칭하기~
N = int(input())
ob = ['I'] + (['O','I']*N)
alen = len(ob)
M = int(input())
qu = list(input())
blen = len(qu)
res = 0
i = 0
# for i in range(blen-alen+1):
while i < (blen-alen+1):
    cnt = 0
    for j in range(alen):
        if qu[i+j] == ob[j]:
            cnt += 1
        else:
            i += j
            break
    if cnt == alen:
        res += 1
    i += 1
print(res)