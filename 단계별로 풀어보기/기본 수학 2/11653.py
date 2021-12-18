n = int(input())
arr = []

if n > 1:
    for i in range(2, n + 1):
        while n % i == 0:
            n = n // i
            arr.append(i)
    for number in arr:
        print(number)
