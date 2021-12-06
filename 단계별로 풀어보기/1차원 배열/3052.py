number = [0 for _ in range(10)]
arr = []
count = 0

for i in range(10):
    number[i] = int(input())

for i in range(10):
    if number[i] % 42 not in arr:
        arr.append(number[i] % 42)
    else:
        pass

print(len(arr))
