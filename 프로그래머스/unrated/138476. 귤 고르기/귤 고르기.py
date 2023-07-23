from collections import defaultdict

def solution(k, tangerine):
    tangerines = defaultdict(int)
    for t in tangerine:
        tangerines[t] += 1
    
    tangerines_list = list(tangerines.values())
    tangerines_list.sort(reverse=True)
    result = 0
    answer = 0
    for tt in tangerines_list:
        if result >= k:
            break
        result += tt
        answer += 1
    

    return answer