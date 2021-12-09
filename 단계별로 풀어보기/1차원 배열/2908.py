import sys
a, b = map(int, (sys.stdin.readline().rstrip()).split(" "))

if a != b and len(str(a)) == 3 and len(str(b)) == 3:
    a = int(str(a)[::-1])
    b = int(str(b)[::-1])

    if a > b:
        print(a)
    else:
        print(b)
