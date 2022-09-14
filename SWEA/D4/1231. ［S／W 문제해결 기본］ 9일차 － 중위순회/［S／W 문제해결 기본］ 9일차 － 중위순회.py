def inorder(n):
    if n:
        inorder(ch1[n])
        print(nod[n], end='')
        inorder(ch2[n])
        
for test_case in range(1,11):
    nodes = int(input())
    

    root = 1
    # 부모를 인덱스로 자식 번호 저장
    nod = [[] for _ in range(nodes+1)]
    ch1 = [0] * (nodes+1)
    ch2 = [0] * (nodes+1)

    for _ in range(nodes):
        node_no, val, *sons = input().split()
        node_no = int(node_no)
        nod[node_no] = val
        for son in sons:
            if ch1[node_no] == 0: # 아직 자식이 없으면
                ch1[node_no] = int(son) # 자식 1로 저장
            else:
                ch2[node_no] = int(son)
    print(f'#{test_case}', end=' ')
    inorder(1)
    print()