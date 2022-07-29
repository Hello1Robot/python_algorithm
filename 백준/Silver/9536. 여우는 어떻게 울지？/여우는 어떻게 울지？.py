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