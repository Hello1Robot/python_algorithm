def dfs(tot, nums): # 재귀를 이용해서 찾기. 문자열에 저장해두기
    global cnt 
    if tot > N: # 만약 값 넘으면 더 만들지 말고 끝내기
        return
    
    if tot == N: # 목표값에 도달하면
        cnt += 1 # 카운트 올려주기
        if cnt == K: # 만약 목표한 순번에 도달하면
            print(nums[:-1]) # 맨 뒤에 '+' 붙어있으니까 그거 빼고 출력
            exit() # 끝내기
    for i in (1,2,3): # 1, 2, 3 순회
        dfs(tot+i, nums+str(i)+'+')

N, K = map(int,input().split())
res_list = []
cnt = 0
dfs(0,'')
print(-1)

