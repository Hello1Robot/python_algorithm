N = int(input())

if N == 2:
    print('CY')
elif N == 1:
    print('SK')
elif (N-2) % 5 ==0 or (N-2) % 5 == 3:
    print('CY')
else:
    print('SK')