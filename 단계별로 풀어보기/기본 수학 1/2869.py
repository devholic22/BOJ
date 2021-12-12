import sys
import math

a, b, v = map(int, (sys.stdin.readline().rstrip()).split(" "))
day = (v - b) / (a - b)
print(math.ceil(day))
