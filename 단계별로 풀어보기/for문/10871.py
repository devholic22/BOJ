import sys

N, X = map(int, sys.stdin.readline().rstrip().split())

value = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(N):
    if value[i] < X:
        print(value[i], end=" ")
