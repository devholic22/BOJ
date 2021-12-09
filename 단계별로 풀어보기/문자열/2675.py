import sys

t = int(input())
arr = []

if(1 <= t <= 1000):
    for i in range(t):
        enter = (sys.stdin.readline().rstrip()).split(" ")
        r = int(enter[0])
        s = enter[1]
        if ((1 <= r <= 8) and (1 <= len(s) <= 20)):
            string = ""
            for j in range(len(s)):
                string += (s[j] * r)
            arr.append(string)

for result in arr:
    print(result)
