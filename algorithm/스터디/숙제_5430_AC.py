# AC에는 R과 D
# R은 배열에 있는 수의 순서를 뒤집는 함수
# D는 첫 번째 수를 버리는 함수
# 배열이 비어있는데 D를 사용한 경우, error 출력
# 명령어를 연속적인 문자열로 받음
# 예를 들면 RDD 라면 R - D - D 시행
# 입력값이 [1,2,3,4]와 같은 형식으로 들어옴
# 빈 형식도 들어옴(중요!)
# [] 를 어떻게 제거할 지... 흠. 일단 문제에서 요구한 형식대로 진행

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cmd = list(input())
    N = int(input())
    # rst = input().replace('[','').replace(']','').strip().split(',') # 좌우 자르고 콤마 기준으로 자르기
    # 슬라이싱으로 대체해볼까?
    rst = list(filter(None, input()[1:-2].split(','))) # 개행문자 때문인지 -2까지 잘라야 되네
    # rst = list(filter(None, rst)) # 빈 값 제거하기.
    # 생각 1. 파이썬의 리버스를 이용하기.
    # 덱이니까, 덱을 사용할까?
    que = deque(rst)
    err_cnt = 0 # 에러 났는지 확인
    for cm in cmd:
        if cm == 'R':
            que.reverse()
        if cm == 'D':
            if que:
                que.popleft()
            else:
                print('error')
                err_cnt = 1
                break
    if not err_cnt:
        print('[',end='')
        print(','.join(que),end='')
        print(']')