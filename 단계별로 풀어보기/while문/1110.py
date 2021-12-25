import sys
n = int(sys.stdin.readline().rstrip())

if (0 <= n <= 99):
    count = 0
    value = n
    arr = []
    while not value in arr:
        arr.append(value)
        first = value // 10
        second = value % 10
        sum = first + second
        count += 1
        value = (second * 10) + (sum % 10)
    print(count)
