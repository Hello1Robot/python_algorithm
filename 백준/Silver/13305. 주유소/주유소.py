# 전형적인 그리디 문제
# 자신보다 싼 주유소가 어디있는지 탐색
# 거기까지 갈 수 있는 기름만 채워가기
cities = int(input()) # 도시들의 수
paths = list(map(int, input().split()))
oils = list(map(int, input().split()))

# 오일의 값을 바꾸는게?
# 만약 [0]이 [1]보다 싸다면 [1]도 [0]의 가격으로 바꿔야
total = 0
for i in range(cities-2):
    if oils[i] < oils[i+1]:
        oils[i+1] = oils[i]
for n in range(len(paths)):
    total += paths[n] * oils[n]

print(total)