from collections import deque


def solution(cacheSize, cities):
    answer = 0
    que = deque()
    for city in cities:
        city = city.lower()
        for i in range(len(que)-1, -1, -1):
            if que[i] == city:
                answer += 1
                que.remove(city)
                break
        else:
            answer += 5
        que.appendleft(city)

        if len(que) > cacheSize:
            que.pop()

    return answer