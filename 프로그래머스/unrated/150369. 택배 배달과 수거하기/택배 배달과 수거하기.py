def solution(cap, n, deliveries, pickups):
    answer = 0
    ac_d = [deliveries[-1]]
    ac_p = [pickups[-1]]
    for i in range(1, n):
        ac_d.append(deliveries[n-i-1]+ac_d[i-1])
        ac_p.append(pickups[n-i-1]+ac_p[i-1])
    
    tot = 0
    start = 0
    while tot < ac_d[-1] or tot < ac_p[-1]:
        for i in range(start, n):
            if ac_d[i] > tot or ac_p[i] > tot:
                start = i
                answer += (n-i)
                break
        tot += cap

        
    
    return answer*2