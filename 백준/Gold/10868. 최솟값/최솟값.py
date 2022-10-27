import math
from sys import stdin
input = stdin.readline

def segment_tree(idx, start, end):
    if start == end: # 리프노드 발견 시 갱신
        seg_list[idx] = nums[start]
        return seg_list[idx]
    
    mid = (start+end) // 2 # 중간값 설정해서 반으로 딱딱 나눠서 트리만들기

    left = segment_tree(idx*2, start, mid)
    right = segment_tree(idx*2+1, mid+1, end)
    
    seg_list[idx] = min(left, right)# min값 재귀를 통해 설정

    return seg_list[idx]

def find_tree(idx, start, end, start_range, end_range):
    if start_range > end or end_range < start:
        return INF
    
    if start_range <= start and end_range >= end:
        return seg_list[idx]
    
    mid = (start+end) // 2
    left = find_tree(idx*2, start, mid, start_range, end_range)
    right = find_tree(idx*2+1, mid+1, end, start_range, end_range)
    return min(left, right)

INF = 1e9+1
N, M = map(int,input().split())
nums = [int(input()) for _ in range(N)]
# math.log(N,2) => log(N)
# math.ceil => 올림
# pow(2, 숫자) => 2^숫자
seg_list = [0]*((pow(2,math.ceil(math.log(N,2))+1))-1)
segment_tree(1, 0, len(nums)-1)

for _ in range(M):
    stt, ed = map(int,input().split())
    stt, ed = stt-1, ed-1
    res = find_tree(1,0,len(nums)-1,stt,ed)
    print(res)