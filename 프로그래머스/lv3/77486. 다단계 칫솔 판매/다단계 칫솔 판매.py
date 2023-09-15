from collections import defaultdict

def solution(enroll, referral, seller, amount):
    answer = [0]*len(enroll)
    idx = defaultdict(int)
    idx["-"] = -1
    for i in range(len(enroll)):
        idx[enroll[i]] = i

    # 추가로 뭘 안해도 찾아지지 않을까?
    # 한번 짜보자
    def dfs(x,money):
        if x == -1:
            return
        
        dt = money // 10
        if dt:
            mine = money - dt
            answer[x] += mine
            dfs(idx[referral[x]], dt)
        else:
            answer[x] += money
    
    for j in range(len(seller)):
        dfs(idx[seller[j]], amount[j]*100)
    
    return answer