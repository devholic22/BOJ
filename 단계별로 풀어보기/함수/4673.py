def get_creater(n):
    sum = n
    n = list(str(n))
    for i in range(len(n)):
        sum += int(n[i])
    return sum


creater_list = []
for i in range(10000):
    creater_list.append(get_creater(i))

for i in range(10000):
    if i not in creater_list:
        print(i)
