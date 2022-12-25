a, b, c = map(int,input().split())

type1 = a * b / c
type2 = a / b * c
print(int(max(type1, type2)))