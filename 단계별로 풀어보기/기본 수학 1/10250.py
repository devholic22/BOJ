import sys

t = int(sys.stdin.readline().rstrip())  # test case
answer_arr = []
for _ in range(t):
    h, w, n = map(int, (sys.stdin.readline().rstrip()).split(" "))
    arr = []
    for i in range(1, w + 1):
        for j in range(1, h + 1):
            if len(str(i)) == 1:
                arr.append(f"{j}0{i}")
            else:
                arr.append(f"{j}{i}")
    answer_arr.append(arr[n - 1])

for result in answer_arr:
    print(result)
