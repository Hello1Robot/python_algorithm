import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)

    while scoville[0] < K:
        new_food = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville, new_food)
        answer += 1
    return answer

