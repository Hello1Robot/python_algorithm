min, sec = map(int,input().split(':'))
click = 0
# 10초단위니까 10으로 나누어서 생각
# 1초 늘리는 버튼
# 3초 늘리는 버튼
# 6초 늘리는 버튼
# 60초 늘리는 버튼
tot_sec = (min*60 + sec)//10

for btn in (60, 6, 3, 1):
    a, b = divmod(tot_sec, btn)
    tot_sec = b
    click += a
    if btn == 3 and a:
        click -= 1


print(click+1)