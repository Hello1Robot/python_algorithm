N = 1000 - int(input())
count = 0
if N >= 500:
   A, B = divmod(N, 500)
   count += A
   N = B
if N >= 100:
   A, B = divmod(N, 100)
   count += A
   N = B
if N >= 50:
   A, B = divmod(N, 50)
   count += A
   N = B
if N >= 10:
   A, B = divmod(N, 10)
   count += A
   N = B
if N >= 5:
   A, B = divmod(N, 5)
   count += A
   N = B
if N >= 1:
   count += N

print(count)