# 스택을 쓰는 문제
# 근데 감이 안잡히긴 함
# 한 번 서치할 때마다 최대값을 찾으면 안되나?
# 안되네 ㅇㅋ;
# N자리 숫자 중 K 개를 지움
# 그럼 처음부터 K 개 중에서 제일 큰 값만 남기면 됨이라는 아이디어
# 이게맞다 ㅇㅇ
# 구체적인 아이디어 설명
# 앞에서 K번째 숫자 중 가장 큰 게 선택됨
# 선택된 숫자에서 다시 K-1번째 숫자까지 확인하고, 가장 큰 숫자를 고름
# K가 0이 될 때 까지 반복
# 아니다 pop한 갯수가 K가 될 때까지?
# pop카운트가 있어야되나

# 아 이거 구현이 너무 어렵네
# 스택을 써서 할 수 있는건가?
# 이중 while문을 쓸까
# 1. K범위 내에서 가장 큰 숫자의 인덱스를 찾음
# 만약 인덱스가 2라면, 0과 1을 pop해야 하니까
# 그만큼 반복을 돌면서 팝 하는데
# 만약 pop_cnt 가 K 가 되면 끝.
# 아니라면 K를 pop_cnt 만큼 빼줌
# 그리고 pop_cnt 초기화

N, K = map(int, input().split())
str1 = list(input())
int_str = list(map(int, str1))
stack = []
search_cnt = 0
pop_cnt = 0
while K > 0 and int_str:
    ans = int_str[0:K]
    max_val = max(ans)
    n = int_str.index(max_val)
    stack.append(int_str[n])
    int_str = int_str[n+1:]
    K -= n

print(stack)

# 이 방식은 좀 곤란하긴 하네
# 다시 생각하기.
# 오늘은 공부해야겠다