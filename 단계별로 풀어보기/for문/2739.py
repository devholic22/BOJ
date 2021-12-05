N = int(input())

if (1 <= N <= 9):
    for i in range(1, 9 + 1):
        print(f"{N} * {i} = " + str(N * i))
