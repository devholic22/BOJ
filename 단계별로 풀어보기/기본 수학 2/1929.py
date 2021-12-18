import sys


def isPrime(x):
    if x == 1:
        return False
    else:
        for test in range(2, int(x**0.5) + 1):
            if x % test == 0:
                return False
        return True


m, n = map(int, (sys.stdin.readline().rstrip()).split(" "))
if (1 <= m <= n):
    for number in range(m, n + 1):
        if isPrime(number):
            print(number)
