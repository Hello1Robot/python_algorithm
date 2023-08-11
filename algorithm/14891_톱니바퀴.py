# deque lotate 써서 돌리고돌리고 하면 되지 않을까 싶기도 하고
# 3-9-3-9-3-9 이거 확인해서 돌아가야 함
from collections import deque
from sys import stdin; input = stdin.readline

def cogSpin(num, cnt, endlist):
    endlist[num] = 1
    if num == 1:
        cog1.rotate(cnt)
        if not endlist[2]:
            if cog1[2] != cog2[6]:
                cogSpin(2,-cnt,endlist)

    elif num == 2:
        cog2.rotate(cnt)
        if not endlist[1]:
            if cog1[2] != cog2[6]:
                cogSpin(1,-cnt,endlist)
        
        if not endlist[3]:
            if cog2[2] != cog3[6]:
                cogSpin(3,-cnt,endlist)

    
    elif num == 3:
        cog3.rotate(cnt)
        if not endlist[2]:
            if cog2[2] != cog3[6]:
                cogSpin(2,-cnt,endlist)
        
        if not endlist[4]:
            if cog3[2] != cog4[6]:
                cogSpin(4,-cnt,endlist)
    
    elif num == 4:
        cog4.rotate(cnt)
        if not endlist[3]:
            if cog3[2] != cog4[6]:
                cogSpin(3,-cnt,endlist)


cog1, cog2, cog3, cog4 = [deque(map(int,input().rstrip())) for _ in range(4)]

N = int(input())
for _ in range(N):
    cog, cnt = map(int,input().split())
    cogSpin(cog, cnt, [0,0,0,0,0])

print(cog1)
print(cog2)
print(cog3)
print(cog4)
print(cog1[0]+(cog2[0]*2)+(cog3[0]*4)+(cog4[0]*8))