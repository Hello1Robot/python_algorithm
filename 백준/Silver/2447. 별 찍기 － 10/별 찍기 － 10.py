def 별찍기(normal):
    stars = []
    for i in range(3*len(normal)):
        if i // len(normal) == 1:
            stars.append(normal[i%len(normal)] + " " * len(normal) + normal[i % len(normal)])
        else:
            stars.append(normal[i%len(normal)] * 3)
    return stars

# 3을 기본단위로 해서 만들기
normal = ['***', '* *', '***']
N = int(input())
# N이 3의 몇 거듭제곱인지 구해야되는데, 함수 못찾겠음. pow?
# 걍 3으로 여러 번 나눠봐야 될듯?
cnt = 0
while N > 3:
    N = N // 3
    cnt += 1

for x in range(cnt):
    normal = 별찍기(normal)

for star in normal:
    print(star)