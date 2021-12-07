def is_han(n):
    n = list(str(n))
    if len(n) >= 3:
        dis = int(n[0]) - int(n[1])
        for i in range(2, len(n)):
            bet = int(n[i - 1]) - int(n[i])
            if bet != dis:
                return False
    return True


n = int(input())
count = 0

if (1 <= n <= 1000):
    for i in range(1, n + 1):
        if is_han(i) == True:
            count += 1
    print(count)
