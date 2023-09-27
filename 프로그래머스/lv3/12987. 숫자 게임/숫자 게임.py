# 10만 이하면, 좀 곤란할듯...?
# 이분탐색을 해볼까
def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    start = 0
    end = len(A)-1
    for b in B:
        if A[start] < b:
            start += 1
            answer += 1
        else:
            end -= 1

    return answer