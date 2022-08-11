N = int(input())
num_list = [input() for _ in range(N)]
num_list.sort(key=lambda x:len(x), reverse=True)
print(num_list)
# 잠시만 아이디어 정리 먼저
# 길이별로 배열?
# 원래 높은 자릿수 먼저 숫자 배열해서
# 제일 큰 수 되도록 하는건데
# 그리디니까 좀 쉽게 생각하는 게 좋겠고
# 거꾸로 뒤집어서 넣을까 했는데
# 이거 그냥 len 차이를 이용해서 해야되나
# len 순으로 배열하고
# len 차이만큼 먼저 배열하기???
# 아니면 while 돌면서 숫자 배열?

# 지금 문제는 뭐냐면
# 같은 순번의 경우에 어떻게 조건을 부여할 지
# 갯수도 세야돼? 어ㅏ휴
# 0 부터 9까지의 range를 이용한 리스트를 만들고
# 기본 False, 사용 중이면 True
# 숫자와 알파벳 구분을 어떻게 할 지 생각해볼까.
# isalpha가 무난하려나


