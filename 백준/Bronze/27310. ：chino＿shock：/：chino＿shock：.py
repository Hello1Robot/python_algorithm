
from sys import stdin;
a = stdin.readline().rstrip()

print(len(a)+a.count(":")+(a.count("_")*5))