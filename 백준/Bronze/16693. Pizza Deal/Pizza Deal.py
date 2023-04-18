from math import pi

a, b = map(int, input().split())
c, d = map(int, input().split())

if b / a < d / (c ** 2 * pi):
    print("Slice of pizza")
else:
    print("Whole pizza")