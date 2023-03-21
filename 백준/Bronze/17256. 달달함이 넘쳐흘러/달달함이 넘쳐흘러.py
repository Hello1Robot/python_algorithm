from sys import stdin; input=stdin.readline
a,b,c = map(int,input().split())
x,y,z = map(int,input().split())
print(x-c, y//b, z-a)