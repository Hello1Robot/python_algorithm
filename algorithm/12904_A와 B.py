def DFS(A,B,f): # DFS를 이용해서 B로 변환할 수 있는지 확인
    if len(A) == len(B): # B의 길이와 같아진다면
        if f: # 만약 뒤집혀있다면
            if A[::-1] == B: # A를 뒤집어서 비교
                print(1) # 성공한다면, 더이상 진행할 필요가 없으니 exit로 탈출
                exit()
        else: # 아니라면
            if A == B: # A와 B를 비교
                print(1)
                exit()
        return
    
    if not f:
        DFS('B'+A, B, 1)
        DFS(A+'A',B,0)
    else:
        DFS(A+'B',B,0)
        DFS('A'+A,B,0)

A = input()
B = input()
DFS(A,B,0)
print(0) # DFS를 돌렸는데도 값이 나오지 않았으면 0을 프린트