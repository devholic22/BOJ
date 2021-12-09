import string
import sys

s = sys.stdin.readline().rstrip()

alpha = string.ascii_uppercase
dict = {}

if s.isalpha():
    s = s.upper()
    for small in s:
        for text in alpha:
            if text == small:
                if dict.get(f"{text}") is not None:
                    dict[f"{text}"] += 1
                else:
                    dict[f"{text}"] = 1

count = [k for k, v in dict.items() if max(dict.values()) == v]

if(len(count) > 1):
    print("?")
else:
    result = (max(dict, key=dict.get))
    print(result)
