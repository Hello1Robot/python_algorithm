from collections import deque

def solution(food_times, k):
    answer = 0
    que = deque(food_times)
    que.rotate(k)
    return answer