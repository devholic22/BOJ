want = [text for text in input()]

if 2 <= len(want) <= 15:
    sec = 0
    case = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

    for w in want:
        for i in range(len(case)):
            if w in case[i]:
                sec += (3 + i)
    print(sec)
