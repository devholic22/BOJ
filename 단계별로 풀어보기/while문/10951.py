import sys

A, B = map(int, sys.stdin.readline().rstrip().split())

if (0 < A < 10 and 0 < B < 10):
    while True:
        try:
            print(A + B)
            A, B = map(int, sys.stdin.readline().rstrip().split())
        except:
            break
