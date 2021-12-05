import sys

N, X = map(int, sys.stdin.readline().rstrip().split())

arr = []

value = sys.stdin.readline().rstrip().split()

for i in range(N):
    if int(value[i]) < X:
        arr.append(value[i])

for result in arr:
    print(result, end=" ")
