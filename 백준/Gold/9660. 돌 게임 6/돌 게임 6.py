N = int(input())

if N == 1:
    print('SK')
elif N == 2:
    print('CY')
elif N%7 == 2 or N%7 == 0:
    print('CY')
else:
    print('SK')