a = int(input())
b = int(input())
c = int(input())

if (100 <= a <= 1000 and 100 <= b <= 1000 and 100 <= c <= 1000):
    value = a * b * c
    data = str(value)  # 17037300
    arr = [i for i in range(0, 9 + 1)]
    result = [0 for _ in range(0, 9 + 1)]

    for i in arr:
        for j in data:
            if str(arr[i]) == j:
                result[i] += 1

    for number in result:
        print(number)
