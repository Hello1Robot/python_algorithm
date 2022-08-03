N = int(input())
friends = {'1/4':0, '1/2':0, '3/4':0}
for _ in range(N):
    n = input()
    if n == '1/2':
        friends[n] += 1
    elif n == '1/4':
        friends[n] += 1
    else:
        friends[n] += 1

# 접근방식이 그냥 합하는 게 아니네
# 1/2는 두 개가 모여서 한 판
# 1/4와 3/4가 두 개 모여서 한 판
# 1/4와 1/2도 두 개가 모이면 한판... 아 개귀찮네 ㅋㅋㅋ;

# 1/2를 2로 나눴을 때 나머지가 있으면 흠
# 2까지 뺄 수 있는데
# 1개만 있을수도 있자너...
# 좀 고민이되네
# 그리디 자너 그리디
# 그리디 스럽게 풀어야돼
# 3/4 갯수 세고
# 그만큼 1/4 갯수 빼고
# 1/2 갯수 세고
# 홀수면 1/4 갯수 빼고
# 만약 1/4가 양수면
# 4로 나누고 몫을 더해주고
# 나머지 있으면 1을 더해줌
# 이럼 코드 좀 길어지나?
cnt = 0
cnt += friends.get('3/4', 0)
friends['1/4'] -= friends.get('3/4', 0)
pz, npz = divmod(friends.get('1/2',0), 2)
cnt += pz
if npz != 0:
    friends['1/4'] -= 2
    cnt += 1
if friends.get('1/4',0) > 0:
    pz2, npz2 = divmod(friends.get('1/4',0), 4)
    cnt += pz2
    if npz2 != 0:
        cnt += 1
print(cnt)