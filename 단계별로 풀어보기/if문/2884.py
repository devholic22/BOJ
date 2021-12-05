h, m = map(int, input().split(" "))

if ((0 <= h <= 23) and (0 <= m <= 59)):
    if m >= 45:
        m -= 45
    else:
        minus_m = 45 - m
        if h != 0:
            h -= 1
        else:
            h = 23
        m = 60 - minus_m
    print(f"{h} {m}")
