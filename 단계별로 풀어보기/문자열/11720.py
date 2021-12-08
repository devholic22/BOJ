n = int(input())
arr = []
value = input()
sum = 0

for data in value:
    arr.append(data)

if (len(arr) == n and (1 <= n <= 100)):
    for i in range(len(arr)):
        sum += int(arr[i])

print(sum)
