import sys
n = int(sys.stdin.readline().rstrip())
number = []
if (1 <= n <= 1000000):
    number = (sys.stdin.readline().rstrip()).split()
    for i in range(len(number)):
        number[i] = int(number[i])
    print(min(number), max(number))
