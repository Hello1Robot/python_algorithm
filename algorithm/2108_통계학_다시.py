N = int(input()) # 받을 숫자 갯수 받아오기
rst = [int(input()) for _ in range(N)]

print(round(sum(rst)/N))
rst.sort()
print(rst[N//2])
rst2 = list(set(rst))
max_cnt = 0
cnt_tups = []
for i in rst2:
    a = rst.count(i)
    cnt_tups.append((a,i))
    if max_cnt < a:
        max_cnt = a
res_list = []
for n in range(len(cnt_tups)):
    if cnt_tups[n][0] == max_cnt:
        res_list.append(cnt_tups[n][1])
res_list.sort()

if len(res_list) > 1:
    print(res_list[1])
else:
    print(res_list[0])

print(rst[-1] - rst[0])
