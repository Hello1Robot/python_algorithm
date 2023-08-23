# 진짜 귀찮은 유형의 문제...
# 그래도 카카오 입사시험에 나온거니까
# 풀긴 풀어야지

# 생각
# 현재 색인을 들고있는 게 맞긴할듯... Z가 26이니까 27부터 집어넣게
# 가장 긴 w를 탐색해야 함. 현재 위치 확인 -> 그다음거랑 이어진 거 있는 지 확인 -> 없으면 현재 위치걸로 펑!
# while을 써서 i값을 움직이는 형식으로 가는 게 나을까? 싶으니까 이렇게 풀어보기
# w를 탐색하는 과정이 제일 중요. A부터 Z까지 초기화 어떻게 할까? -> 이거 좀 세련된 방법 있는디;

from collections import defaultdict

def solution(msg):
    answer = []
    idxs = defaultdict(int)

    for i in range(26):
        idxs[chr(ord('A')+i)] = i+1
    
    now_idx = 27
    now = 0
    while now < len(msg):
        next = 1
        while now+next <= len(msg):
            if idxs[msg[now:now+next]]:
                next+=1
            else:
                break
        answer.append(idxs[msg[now:now+next-1]])
        idxs[msg[now:now+next]] = now_idx
        now_idx += 1
        now = now + next - 1

    return answer