from sys import stdin
from math import ceil, log
input = stdin.readline

def check_pm(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0

def segment_tree(idx, start, end):
    if start == end: # 리프노드 발견 시 갱신
        seg_list[idx] = check_pm(nums[start])
        return seg_list[idx]
    
    mid = (start+end) // 2 # 중간값 설정해서 반으로 딱딱 나눠서 트리만들기

    left = segment_tree(idx*2, start, mid)
    right = segment_tree(idx*2+1, mid+1, end)
    
    seg_list[idx] = left * right

    return seg_list[idx]

def find_tree(idx, start, end, start_range, end_range):
    if start_range > end or end_range < start:
        return 1
    
    if start_range <= start and end_range >= end:
        return seg_list[idx]
    
    mid = (start+end) // 2
    left = find_tree(idx*2, start, mid, start_range, end_range)
    right = find_tree(idx*2+1, mid+1, end, start_range, end_range)
    return left*right

def tree_update(i, start, end, idx, diff):
    if start > idx or end < idx:
        return
    
    if start == end:
        seg_list[i] = diff
    else:
        mid = (start+end) // 2
        tree_update(i*2, start, mid, idx, diff)
        tree_update(i*2+1, mid+1, end, idx, diff)
        seg_list[i] = seg_list[2*i] * seg_list[2*i+1]

while True:
    try:
        N, K = map(int,input().split())
        nums = list(map(int,input().split()))
        # math.log(N,2) => log(N)
        # math.ceil => 올림
        # pow(2, 숫자) => 2^숫자
        seg_list = [0]*(2**(ceil(log(N,2)+1)))
        segment_tree(1, 0, len(nums)-1)
        ans = ''

        for _ in range(K):
            cmd, a, b = input().split()
            if cmd == 'P':
                stt, ed = int(a)-1, int(b)-1
                res = find_tree(1,0,len(nums)-1,stt,ed)
                if res > 0:
                    ans += '+'
                elif res == 0:
                    ans += '0'
                elif res < 0:
                    ans += '-'
            else:
                a, b = int(a), int(b)
                b = check_pm(b)
                nums[a-1] = b
                tree_update(1, 0, len(nums)-1, a-1, b)

        print(ans)
    except Exception:
        break