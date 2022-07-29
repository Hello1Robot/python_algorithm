# 어떻게 하면 깔끔하게 리스트에서 중복되는 값을 제거할 수 있을지에 대한 고민
# 사실 하나 만들어놓으면 좋을거같음...
# 원래는 딕셔너리에 넣어서 메모리 줄이려고 하는데
# 이번에는 스트링으로 받은 값을 list comprehense로 변환하는데
# 이걸 딕셔너리로 변환할 수 있을까
# 할 순 있는데 깔끔한가
# if문을 한줄로 쓰는 걸로 한번 해볼까

T = int(input())
for test_case in range(1, T+1):
    pow = input().split()
     
    powpow = []
    while True:
        N = input()
        if N == 'what does the fox say?':
            break
        bow = N.split()
        powpow.append(bow[-1])

    new_pow = [i for i in pow if i not in powpow]
    for i in new_pow:
        print(i, end = " ")
    print()
