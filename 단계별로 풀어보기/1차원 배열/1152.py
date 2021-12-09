import sys
text = (sys.stdin.readline().rstrip()).split(" ")
for value in text:
    if value == "":
        text.remove(value)
count = len(text)
print(count)
