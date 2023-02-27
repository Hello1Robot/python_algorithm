# 하나라도 숫자가 있는 날짜를 세는 문제
# 가장 큰 숫자만큼 배열을 만들던가 어쩌구저쩌구 하면 됨
# 365니까 범위가 좀 적음
# 그냥 길이만큼 visited 만들고 구간합 하면 될듯?
# 구간합으로 푸는 문제라고 생각함 결국
# 그래서 결과적으로 지는 날은 안주어져있기 때문에
# 앞 순서에 1, 뒤에는 -1 해서 돈 다음에
# 숫자가 있는 데를 세면 됨
def solution(flowers):
    DP = [0]*366
    for start, end in flowers:
        DP[start] += 1
        DP[end] -= 1
    tot = [0]*366
    zero_cnt = 0
    for i in range(1,366):
        tot[i] = tot[i-1]+DP[i]
        if tot[i] == 0:
            zero_cnt += 1
    
    
    answer = 365-zero_cnt

    return answer