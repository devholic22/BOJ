m = int(input())
n = int(input())
arr = []

for number in range(m, n + 1):
    count = 0
    if number > 1:
        for test in range(2, number):
            if number % test == 0:
                count -= 1
                break
        if count == 0:
            arr.append(number)

if len(arr) > 0:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)
