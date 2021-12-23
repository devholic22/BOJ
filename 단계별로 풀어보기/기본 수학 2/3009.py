arr_x = []
arr_y = []

for _ in range(3):
    x, y = map(int, input().split(" "))
    if x not in arr_x:
        arr_x.append(x)
    else:
        arr_x.remove(x)
    if y not in arr_y:
        arr_y.append(y)
    else:
        arr_y.remove(y)
answer = f"{arr_x.pop()} {arr_y.pop()}"
print(answer)
