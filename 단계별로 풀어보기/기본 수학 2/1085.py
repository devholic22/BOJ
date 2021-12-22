import sys
x, y, w, h = map(int, (sys.stdin.readline().rstrip()).split(" "))

top_y = h - y
bottom_y = y
left_x = x
right_x = w - x

print(min(top_y, bottom_y, left_x, right_x))
