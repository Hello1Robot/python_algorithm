# 단어 하나가 떨어져 있는지를 확인해야 됨!
# set 활용을 해봐?
# 1. 연속된 문자열을 없앤다.
# 2. 확인한다.
# 이렇게 해도 됨.

N = int(input())
cnt = 0
for _ in range(N):
    rst = list(input())
    new_rst = []
    if len(rst) == 1:
        cnt += 1
        continue

    for i in range(len(rst)-1):
        if rst[i] == rst[i+1]:
            continue
        else:
            new_rst.append(rst[i])
    new_rst.append(rst[-1])
    길이 = len(new_rst)
    rst_set = set(new_rst)
    셋길이 = len(rst_set)

    if 길이 == 셋길이:

        cnt += 1
print(cnt)