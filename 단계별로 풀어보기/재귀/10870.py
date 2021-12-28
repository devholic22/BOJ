dict = {
    0: 0,
    1: 1,
    2: 1
}


def fibonacci(n):
    if n in dict:
        return dict[n]
    else:
        result = fibonacci(n - 1) + fibonacci(n - 2)
        dict[n] = result
        return result


x = int(input())
print(fibonacci(x))
