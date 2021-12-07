import sys
case = int(sys.stdin.readline().rstrip())
result = []

for i in range(case):
    data = (sys.stdin.readline().rstrip()).split()
    student_number = int(data[0])
    data = data[1:]
    sum = 0
    correct_student = 0

    if (1 <= student_number <= 1000):
        for n in range(len(data)):
            sum += int(data[n])
        avg = sum / student_number
        for n in range(len(data)):
            if int(data[n]) > avg:
                correct_student += 1
        result.append(correct_student / student_number * 100)

for value in result:
    print(format(value, ".3f") + "%")
