import sys
n = int(sys.stdin.readline().rstrip())

if(0 <= n <= 1000):
    score = [0 for i in range(n)]
    score_input = (sys.stdin.readline().rstrip()).split()

    for i in range(len(score)):
        if int(score_input[i]) > 100 or int(score_input[i]) < 0:
            pass
        else:
            score[i] = int(score_input[i])
    high = max(score)

    for i in range(len(score)):
        score[i] = score[i] / high * 100

    avg = sum(score) / n
    print(avg)
