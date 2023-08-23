from collections import defaultdict

def solution(msg):
    answer = []
    idxs = defaultdict(int)

    for i in range(26):
        idxs[chr(ord('A')+i)] = i+1                 # A - Z 까지 값 초기화 (1부터 26)
    
    now_idx = idxs['Z']+1                           # 그 다음으로 올 인덱스
    now = 0                                         # 현재 포인터 위치
    while now < len(msg):                           # 포인터가 범위 안에 있을 때 까지만
        next = 1                                    # 탐색 범위 초기화
        while now+next <= len(msg):                 # 탐색 범위가 msg 범위 안에 있도록 설정
            if idxs[msg[now:now+next]]:             # 다음 길이의 단어가 사전에 있으면
                next+=1                             # 탐색 범위 확장
            else:
                break                               # w 탐색 종료
        answer.append(idxs[msg[now:now+next-1]])    # 가장 긴 단어의 색인값 answer에 추가하기
        idxs[msg[now:now+next]] = now_idx           # 가장 긴 단어 + 1 의 단어 색인에 추가하기
        now_idx += 1                                # 다음 색인값 갱신
        now = now + next - 1                        # 포인터 이동

    return answer