# n개의 구간으로 나뉨
# 자동차, 자전거, 대중교통, 도보로 이동할 때 걸리는 시간이 정해져 있음
# 상황에 따라 구간별로 시간이 다를 수 있음
# 각 구간은 하나의 교통수단으로만 이동
# 자동차 : 처음부터 끝까지 자동차로
# 자전거 : 자전거 or 도보
# 도보 : 연속해서 m분만 걸을 수 있음
# 대중교통 : 대중교통 or 도보. 못가는곳도 있음
# infos의 0번 인덱스만 더하면 자동차. 이게 기준점
# 만약 이번과 다음거까지 합쳤는데도 m보다 작으면, 도보 계속할 수 있음


def solution(infos, m):
    sections = len(infos) # 구간 수
    car_cnt = 0 # 자동차는 값 더하기
    cycle = [] # 자전거
    walk = [] # 걷기
    bus = [] # 버스
    cycle_DP = [0]*(sections) # 계산한 값 모아둘 DP
    bus_DP = [0]*(sections)
    for info in infos: # 리스트에 값 채워넣기
        car, cy, bu, wa = info
        if wa > m: # 만약 못걷는거리면, 큰 수 집어넣어둠
            wa = 1e7
        car_cnt += car # 자동차는 바로바로 더하기
        cycle.append(cy)
        bus.append(bu)
        walk.append(wa)
    
    cycle_DP[0] = min(cycle[0], walk[0]) # 자전거 첫 번째는 둘 중 작은 값
    if bus[0] != -1: # 버스가 운행할 수 있으면
        bus_DP[0] = min(bus[0], walk[0])
    else: # 운행못할 경우
        if walk[0] > m: # 걷지도 못하면, 버스 못타는 경우임
            bus_DP[0] = 1e7
        else:
            bus_DP[0] = walk[0]

    for i in range(1, sections):
        if cycle[i] <= walk[i]: # 자전거가 효율적이면 자전거 타기
            cycle_DP[i] = cycle[i]
        else: # 걷는게 더 나을 경우
            if cycle[i-1] > walk[i-1]: # 이전에 걸었는지 자전거 탔는지 확인. 걸었을 경우
                if (walk[i] + walk[i-1]) <= m: # 둘 다 걸어도 된다면
                    cycle_DP[i] = walk[i] # 걷기
                else: # 둘 중 하나만 걸어야 한다면, 둘 중 효율적인 것만 걷기로 하고 나머지는 자전거타기
                    if (cycle[i-1]-walk[i-1]) >= (cycle[i]-walk[i]):
                        cycle_DP[i] = cycle[i]
                    else:
                        cycle_DP[i] = walk[i]
                        cycle_DP[i-1] = cycle[i-1]
            else:
                cycle_DP[i] = walk[i]

    if bus_DP[0] != 1e7: # 버스를 탈 수 있으면
        for i in range(1, sections): 
            if bus[i] != -1: # 만약 버스가 운행한다면
                if bus[i] <= walk[i]: # 버스가 더 효율적이면 버스타기
                    bus_DP[i] = bus[i]
                else: # 아닐 경우
                    if bus[i-1] != -1: # 이전에 버스가 운행하면
                        if bus[i-1] > walk[i-1]: # 이전에 걸었을 경우
                            if (walk[i]+walk[i-1]) <= m: # 둘 다 걸을 수 있으면, 걷기
                                bus_DP[i] = walk[i]
                            else: # 안될경우 둘 중 좀 더 이득인 쪽만 걷기
                                if (bus[i-1]-walk[i-1]) >= (bus[i]-walk[i]):
                                    bus_DP[i] = bus[i]
                                else:
                                    bus_DP[i] = walk[i]
                                    bus_DP[i-1] = bus[i-1]
                        else: # 이전에 버스를 탔을 경우
                            bus_DP[i] = walk[i]
                    else: # 이전에 버스가 운행안하면
                        if (walk[i-1]+walk[i]) <= m: # 둘 다 걸을 수 있으면 걷자
                            bus_DP[i] = walk[i]
                        else: # 아니면 버스타자
                            bus_DP[i] = bus[i]
            else: # 만약 버스가 운행안한다면
                if bus[i-1] == -1: # 만약 이전노선도 운행 안했으면
                    if (walk[i-1]+walk[i]) <= m: # 둘다 걸을 수 있으면 걷기
                        bus_DP[i] = walk[i]
                    else: # 아니면 버스는 못타는거임
                        bus_DP[i] = 1e7
                        break
                else: # 이전엔 운행했으면
                    if (walk[i-1] + walk[i]) <= m: # 둘다 걸을 수 있으면 걷기
                        bus_DP[i] = walk[i]
                    else: # 아닐 경우
                        if bus[i-1] <= walk[i-1]: # 이득인 쪽이 걷기
                            bus_DP[i] = walk[i]
                        else:
                            bus_DP[i-1] = bus[i-1]
                            bus_DP[i] = walk[i]
    
    max_bus = sum(bus_DP)
    max_cycle = sum(cycle_DP)
    answer = min(car_cnt, max_bus, max_cycle)
    
    return answer