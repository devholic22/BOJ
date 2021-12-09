import string

s = input()
arr = string.ascii_lowercase
result = []

if len(s) <= 100 and s.islower():
    for text in arr:
        result.append(s.find(text))

for data in result:
    print(data, end=" ")
