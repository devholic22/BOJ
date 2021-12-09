n = int(input())
count = 0
arr = []

for i in range(n):
    case = list(input())
    init = case[0]
    arr.append(init)
    for j in range(len(case)):
        if case[j] == init:
            pass
        else:
            if case[j] not in arr:
                arr.append(case[j])
                init = case[j]
            else:
                count -= 1
                break
    count += 1
    arr = []
print(count)
