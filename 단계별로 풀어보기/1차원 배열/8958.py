case_number = int(input())
result = []

for i in range(case_number):
    value = 0
    count = 1
    case = input()
    arr = list(case)
    if 0 < len(arr) < 80:
        for j in range(len(arr)):
            if arr[j] == 'O':
                value += count
                count += 1
            else:
                count = 1
    result.append(value)

for data in result:
    print(data)
