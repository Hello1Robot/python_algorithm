# 저축을 잔디 심는것처럼 하는 문제
# 저축일, 1일1잔디 성공 여부만 확인하면 되는 문제니까
# 숫자로 변환해서 다시 날짜로 변환하는 작업을 할 필요는 없음
# 0001:01:01:01:01:01 형태
# 1분은 60초
# 1시간은 60분
# 1일은 24시간
# 1달은 30일
# 사실 일수까지만 파악하면 됨
# s에다가 그 다음 time이 나오기 때문
# 다 돌았을 때 그 다음 타임이 되는지 안되는지 확인하긴데?
# : 를 기준으로 스플릿해서 필요한 값 뽑아내기
# 숫자 계산하기
# 숫자 계산한 것을 토대로 하루가 비는지 아닌지 확인하는 간단한 수학문제 같음
# 하루는 86400초
# s의 날짜는 쓸 필요없음
# 뒤에는 써서 계산
# 시간 * 3600 분 * 60 해서 다 초로 만들기
# 딱 떨어지는 경우를 생각해야되네...
# 86400 인데 day도 now도 0이면 +1 더해야되나?

def solution(s, times):
    slist = list(map(int, s.split(':')))
    flag = 1
    start_day = slist[2]

    now = slist[3]*3600 + slist[4]*60 + slist[5]
    for time in times:
        time_list = list(map(int, time.split(':')))
        seconds = time_list[0]*86400 + time_list[1]*3600 + time_list[2]*60+time_list[3]
        saving_point = now + seconds
        day, now = divmod(saving_point, 86400)

        start_day += day
        if day > 1:
            flag = 0

            
    
    tot_saving = (start_day - slist[2])+1
    answer = [flag, tot_saving]

    return answer

print(solution("2021:04:12:16:08:35", ["01:06:30:00", "01:04:12:00"]))
print(solution("2021:04:12:16:08:35", ["01:06:30:00", "00:01:12:00"]))
print(solution(
"2021:04:12:16:10:42", ["01:06:30:00"]))
print(solution("2021:04:12:16:08:35", ["01:06:30:00", "01:01:12:00", "00:00:09:25"]))
