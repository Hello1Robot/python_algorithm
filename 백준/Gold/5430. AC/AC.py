# 시간초과가 떠서, 뭐가 문제일지 새로 한번 짜 봄
import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cmd = list(input())
    N = int(input())
    # 필터를 쓸 경우는 N이 0일 때 뿐인데?
    rst = input()[1:-2].split(',')
    if N == 0:
        rst = []
    que = deque(rst)
    err_cnt = 0 # 에러 났는지 확인
    # 리버스가 여러 번 있을 경우를 생각해보자.
    # 리버스가 시간복잡도가 드럽게 높으니까
    # 만약에 쓸데없이 RRRRRR 이런 코드 있으면
    # 괜히 6번 뒤집어뒤집어뒤집어 해야됨
    # 사실 Reverse는 홀수번 있는 거 확인만 하면 됨
    # 1과 -1로 확인하면 될 거 같음
    # 그래서 어차피 큐 쓰는거니까, pop과 popleft를 스위칭하면서 사용하면 됨
    rev_cnt = 1
    for cm in cmd:
        if cm == 'R':
            rev_cnt *= -1
        if cm == 'D':
            if que:
                if rev_cnt == 1:
                    que.popleft()
                else:
                    que.pop()
            else:
                print('error')
                err_cnt = 1
                break
    if rev_cnt == -1:
        que.reverse()
    if not err_cnt:
        print('[',end='')
        print(','.join(que),end='')
        print(']')