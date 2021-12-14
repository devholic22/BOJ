def get_sum(dict, pos):
    sum = 0
    for i in range(pos):
        sum += dict[i + 1]
    return sum


result = []
t = int(input())
for i in range(t):

    k = int(input())
    n = int(input())
    arr = [{} for i in range(k + 1)]
    sum = 0
    for i in range(14):
        arr[0][i + 1] = i + 1
    if (1 <= k, n <= 14):
        for j in range(1, k + 1):
            for m in range(1, n + 1):
                arr[j][m] = get_sum(arr[j - 1], m)
    result.append(arr[k][n])

for value in result:
    print(value)
