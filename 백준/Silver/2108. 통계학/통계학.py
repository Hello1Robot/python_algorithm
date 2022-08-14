# 처음에 딕셔너리로 받으면
# 약간 set으로 받는 것처럼
# 문제가 생기는거지...
# 처음 sums에서 문제가 생김
# 근데 해결한 거 같은데 왜 안될까...

N = int(input())

nums_dict = {} # 각 요소의 갯수 카운팅을 위한 딕셔너리 생성
nums_list = [] # 요소를 받아올 리스트
for i in range(N): # 리스트와 딕셔너리에 값 넣기
    a = int(input())
    nums_list.append(a)
    if a in nums_dict:
        nums_dict[a] += 1

    else:
        nums_dict[a] = 1

 
sums = round(sum(nums_list)/N) # 1) 산술평균 구하기

nums_list.sort() # 받은 값들 오름차순 정렬하기
center = nums_list[N//2] # 2) 중앙값 구하기
# 최빈값 구하는 거 주의
# 최빈값 중 두 번째로 작은 값을 출력하라는데...
# 흠 for문을 두 번 돌리는게 의미가 있을까
max_q = 0
for a, b in nums_dict.items():
    if b > max_q:
        max_q = b
w_list = []
for a, b in nums_dict.items():
    if b == max_q:
        w_list.append(a)

w_list.sort()
if len(w_list) > 1: # 3) 길이에 따라서 최빈값 구하기. 하나일 때는 그거, 두 개 이상이면 2번째 거
    rat = w_list[1]
else:
    rat = w_list[0]
ran = nums_list[-1] - nums_list[0] # 4) 범위 구하기
print(sums)
print(center)
print(rat)
print(ran)