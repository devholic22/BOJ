import sys
n = int(input())
count = 0
test = 0

if (1 <= n <= 100):
    number = sys.stdin.readline().rstrip().split(" ")
    if len(number) == n:
        for num in number:
            if 1 <= int(num) <= 1000:
                if int(num) == 1:
                    continue
                for value in range(2, int(num)):
                    if int(num) % value == 0:
                        test -= 1
                if test == 0:
                    count += 1
            test = 0
        print(count)
