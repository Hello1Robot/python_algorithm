N = int(input())

# 초기 전구 상태 받아오기
first_lamp = [int(x) for x in input()]
first_lamp2 = first_lamp[:] # 1차원리스트니까 그냥 얕은복사
# 스플릿으로 나누는 건, 각 자리에 접근해서 데이터의 수정을 용이하기 위해서.
# 목표 전구 상태 받아오기
result_lamp = [int(y) for y in input()]
result_lamp2 = result_lamp[:]
cnt = 1 # 스위치 누르는 숫자 세는 카운트
cnt2 = 0
# 두 전구 값 비교하면서 for문 짜보기
# 0을 눌렀을 경우부터 작성

# 근데 0일 때 1로, 1일 때 0으로 어떻게 만들까?
# if 문을 쓰는 게 깔끔한가?
# 근데 구현할 때 계속 쓸 거 같은데, list comprehension 사용해보자 - 여기서 문제가 있나? 어지럽네 = 문제없는걸로 확인됨. 일단 그냥 둠
# case1의 경우.
# 아니 case2는 새로하나 해야되나? 일단 1 다 짜보고 생각함
# 일단 정답 만들고싶으니까 복붙해서 하나 더만듦.
# 0번을 눌리고 시작하니까 0번과 1번 인덱스 값을 변환
if first_lamp[0] == 1:
    first_lamp[0] -= 1
else:
    first_lamp[0] += 1
if first_lamp[1] == 1:
    first_lamp[1] -= 1
else:
    first_lamp[1] += 1
# first_lamp[0] == 1 if first_lamp[0] == 0 else first_lamp[0] == 0
# first_lamp[1] == 1 if first_lamp[1] == 0 else first_lamp[1] == 0
for i in range(1, N):
    # 앞의 숫자가 같은 경우는 스위치를 누르지 않기
    if first_lamp[i-1] == result_lamp[i-1]:
        continue
    else :
        # 만약 마지막 숫자일 경우에 예외처리
        if i == N-1:
            # first_lamp[i-1] == 1 if first_lamp[i-1] == 0 else first_lamp[i-1] == 0
            # first_lamp[i] == 1 if first_lamp[i] == 0 else first_lamp[i] == 0
            if first_lamp[i-1] == 1:
                first_lamp[i-1] -= 1
            else:
                first_lamp[i-1] += 1
            if first_lamp[i] == 1:
                first_lamp[i] -= 1
            else:
                first_lamp[i] += 1
            cnt += 1
        # 이외의 경우 스위치 누르기
        else:
            # first_lamp[i-1] == 1 if first_lamp[i-1] == 0 else first_lamp[i-1] == 0
            # first_lamp[i+1] == 1 if first_lamp[i+1] == 0 else first_lamp[i+1] == 0
            # first_lamp[i] == 1 if first_lamp[i] == 0 else first_lamp[i] == 0
            if first_lamp[i-1] == 1:
                first_lamp[i-1] -= 1
            else:
                first_lamp[i-1] += 1
            if first_lamp[i] == 1:
                first_lamp[i] -= 1
            else:
                first_lamp[i] += 1
            if first_lamp[i+1] == 1:
                first_lamp[i+1] -= 1
            else:
                first_lamp[i+1] += 1
            cnt += 1

for i in range(1, N):
    # 앞의 숫자가 같은 경우는 스위치를 누르지 않기
    if first_lamp2[i-1] == result_lamp2[i-1]:
        continue
    else :
        # 만약 마지막 숫자일 경우에 예외처리
        if i == N-1:
            # first_lamp[i-1] == 1 if first_lamp[i-1] == 0 else first_lamp[i-1] == 0
            # first_lamp[i] == 1 if first_lamp[i] == 0 else first_lamp[i] == 0
            if first_lamp2[i-1] == 1:
                first_lamp2[i-1] -= 1
            else:
                first_lamp2[i-1] += 1
            if first_lamp2[i] == 1:
                first_lamp2[i] -= 1
            else:
                first_lamp2[i] += 1
            cnt2 += 1
        # 이외의 경우 스위치 누르기
        else:
            # first_lamp[i-1] == 1 if first_lamp[i-1] == 0 else first_lamp[i-1] == 0
            # first_lamp[i+1] == 1 if first_lamp[i+1] == 0 else first_lamp[i+1] == 0
            # first_lamp[i] == 1 if first_lamp[i] == 0 else first_lamp[i] == 0
            if first_lamp2[i-1] == 1:
                first_lamp2[i-1] -= 1
            else:
                first_lamp2[i-1] += 1
            if first_lamp2[i] == 1:
                first_lamp2[i] -= 1
            else:
                first_lamp2[i] += 1
            if first_lamp2[i+1] == 1:
                first_lamp2[i+1] -= 1
            else:
                first_lamp2[i+1] += 1
            cnt2 += 1

if first_lamp == result_lamp and first_lamp2 == result_lamp2:
    print(min(cnt, cnt2))
elif first_lamp == result_lamp and first_lamp2 != result_lamp2:
    print(cnt)
elif first_lamp != result_lamp and first_lamp2 == result_lamp2:
    print(cnt2)
else:
    print(-1)