from itertools import combinations_with_replacement
from math import factorial
n = 6
answer = 0

ab = len(list(combinations_with_replacement(range(6), 5)))

print(ab)

bb = int(factorial(2*n - 2) / (factorial(n-1)*factorial(n-1)))
print(bb)
# for i in range(1,n+1):
#     ab = list(combinations_with_replacement(range(1,n+1), i))
#     for a in ab:
#         if sum(a) <= 6:
#             answer += 1

# print(answer)