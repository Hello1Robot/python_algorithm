A, B, C = int(input()), int(input()), int(input())

if A+B+C != 180:
    print('Error')
    
elif A == B == C :
    print('Equilateral')

elif A == B or A == C or B == C :
    print('Isosceles')

else:
    print('Scalene')