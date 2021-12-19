def getPrime(x):
    arr = []
    if x == 1:
        return False
    for test in range(2, int(x ** 0.5) + 1):
        if x % test == 0:
            return False
    return True


all = list(range(2, 246912))
arr = []

for i in all:
    if getPrime(i):
        arr.append(i)

n = int(input())

while True:
    count = 0
    if n == 0:
        break
    for i in arr:
        if n < i <= 2 * n:
            count += 1
    print(count)
    n = int(input())
