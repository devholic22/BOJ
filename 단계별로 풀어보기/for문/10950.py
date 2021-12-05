t = int(input())

result = []

for _ in range(t):
    a, b = map(int, input().split(" "))
    result.append(a + b)

for value in result:
    print(value)
