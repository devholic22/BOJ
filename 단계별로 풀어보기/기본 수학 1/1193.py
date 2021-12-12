import sys

x = int(sys.stdin.readline().rstrip())
arr = []
sum = 0
add = 1

while sum < x:
    sum += add
    add += 1

stage = add - 1
prev = sum - stage

if stage % 2 == 0:
    left = 1
    right = stage
    while left <= stage:
        arr.append(f"{left}/{right}")
        left += 1
        right -= 1
else:
    left = stage
    right = 1
    while right <= stage:
        arr.append(f"{left}/{right}")
        left -= 1
        right += 1

print(arr[x - prev - 1])
