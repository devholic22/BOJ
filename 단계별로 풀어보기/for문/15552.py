import sys
t = int(sys.stdin.readline().rstrip())

if (t <= 1000000):
    for _ in range(t):
        a, b = map(int, (sys.stdin.readline().rstrip()).split())
        if (1 <= a and b <= 1000):
            print(a + b)
