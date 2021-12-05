import sys

first_number = sys.stdin.readline().rstrip()
second_number = sys.stdin.readline().rstrip()

if len(str(first_number)) and len(str(second_number)) == 3:
    first_stage = int(first_number) * int(str(second_number)[-1])
    second_stage = int(first_number) * int(str(second_number)[-2])
    third_stage = int(first_number) * int(str(second_number)[-3])

    result = first_stage + (second_stage * 10) + (third_stage * 100)

    print(first_stage)
    print(second_stage)
    print(third_stage)
    print(result)
