n = int(input())
count = 1
add = 6
init = 1

while init < n:
    count += 1
    init += add
    add += 6

print(count)
