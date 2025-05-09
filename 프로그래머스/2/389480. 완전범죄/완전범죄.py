def solution(info, n, m):
    # 조건정리 먼저 들어가자
    # 일단 A가 최소가 되도록 해야 함
    # 전부 훔쳐야 하고, 전부 훔치지 못할 경우에는 -1 반환
    # info를 순회해야 하는데, 어떤 순서로 순회할 지도 고민해봐야 할까?
    # 순서가 중요한 지 생각해보자
    # 머리가 굳었네... 이런 경우는 DP인가?
    # 완탐하면서, A 최신화하면 될 듯?
    answer = 1000
    visited = set()
    
    def 재귀(idx, now_a, now_b):
        visited.add((idx, now_a, now_b))
        nonlocal answer
        if(now_a >= answer): return
        
        if(idx == len(info)):
            answer = now_a
            return
        
        if((now_a + info[idx][0]) < n and (idx+1, now_a + info[idx][0], now_b) not in visited ):
            재귀(idx+1, now_a + info[idx][0], now_b)

        if((now_b + info[idx][1]) < m and (idx+1, now_a, now_b + info[idx][1]) not in visited):
            재귀(idx+1, now_a, now_b + info[idx][1])

    재귀(0,0,0)

    if(answer == 1000): answer = -1

    return answer


