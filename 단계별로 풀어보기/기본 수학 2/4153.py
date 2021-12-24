while True:
    arr = list(map(int, input().split(" ")))
    large = max(arr)
    if sum(arr) == 0:
        break
    arr.remove(large)
    if arr[0] ** 2 + arr[1] ** 2 == large ** 2:
        print("right")
    else:
        print("wrong")
