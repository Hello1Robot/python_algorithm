from sys import stdin; input = stdin.readline

def multi (a,n):
  if n == 1:
      return a%c
  else:
      tmp = multi(a,n//2)
      if n %2 ==0:
          return (tmp * tmp) % c
      else:
          return (tmp  * tmp *a) %c

a,b,c = map(int, input().split())
          
print(multi(a,b))