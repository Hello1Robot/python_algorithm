def 별찍기(slen):
    stars = [] # 새로운 별들을 담을 리스트
    for i in range(3*slen):
        if i // slen == 1:
            stars.append(normal[i%slen] + " " * slen + normal[i % slen])
        else:
            stars.append(normal[i%slen] * 3)
    return stars

# 3을 기본단위로 해서 만들기
normal = ['***', '* *', '***']
N = int(input())
# N이 3의 몇 거듭제곱인지 구해야되는데, 함수 못찾겠음. pow?
# 걍 3으로 여러 번 나눠봐야 될듯?
cnt = 0
while N > 3: # 3이면 그냥 normal 프린트하면 됨
    N = N // 3
    cnt += 1

# 시작길이는 3으로 시작
star_len = 3
for x in range(cnt):
    normal = 별찍기(star_len)
    star_len *= 3 # 돌 때마다 3 곱해주기

for star in normal:
    print(star)