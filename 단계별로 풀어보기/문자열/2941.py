import sys

question = sys.stdin.readline().rstrip()
voca = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

if len(question) <= 100:
    for t in voca:
        while t in question:
            if t in question:
                question = question.replace(t, '/', 1)
                count += 1

    question = question.split('/')

    for value in question:
        if value == '':
            pass
        else:
            count += len(value)

    print(count)
