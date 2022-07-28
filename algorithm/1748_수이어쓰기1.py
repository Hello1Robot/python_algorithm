import sys

N = int(sys.stdin.readline())
total = ''
for i in range(1,N+1):
    total = total + str(i)

sys.stdout.write(str(len(total)))

