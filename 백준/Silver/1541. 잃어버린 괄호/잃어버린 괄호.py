# 기본적인 아이디어
# 마이너스는 다음 마이너스가 나올 때 까지 묶으면 됨
# 그럼 마이너스 하나 이후에는 모든 값이 -라고 생각하면 됨
# 숫자를 어떻게 추출하느냐가 아이디어.
# + 기준으로 모든 숫자를 나눔
# - 가 나오면, 이후 숫자는 모두 빼기

st = input()
idx = st.find('-')
plus_ = ''
minus_ = ''
if idx != -1:
    plus_ = st[0:idx]
    minus_ = st[idx+1:]
    plus2 = plus_.replace('-', '+')
    minus2 = minus_.replace('-', '+')
    plus_list = plus2.split('+')
    minus_list = minus2.split('+')
    new_plus = list(map(int, plus_list))
    new_minus = list(map(int, minus_list))
    print(sum(new_plus)-sum(new_minus))
else:
    res = st.split('+')
    res = list(map(int, res))
    print(sum(res))
