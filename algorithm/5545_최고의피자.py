N = int(input())
dough, topping = map(int, input().split())
dough_cal = int(input())
topping_cal_list = [int(input()) for _ in range(N)]
# 칼로리 높은 순으로 정렬
topping_cal_list.sort(reverse=True)
# N+1 가지 경우로 나누어서 생각해보자.
# 1. 도우만 있을 때의 열량
# 2. 도우+1 가지 있을 때의 열량 (...) + 도우+N가지 있을 때의 열량
# 도우열량의 평균부터 토핑 하나씩 올릴때의 평균을 비교해서 값을 구한다.
max_cal = dough_cal
avr_cal = max_cal / dough
max_avr = avr_cal
for i in range(len(topping_cal_list)):
    max_cal += topping_cal_list[i]
    A = max_cal / (dough + (topping * (i+1)))
    if A > max_avr:
        max_avr = A
print(int(max_avr))
