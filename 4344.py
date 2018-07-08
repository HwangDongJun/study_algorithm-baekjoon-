#평균은 넘겠지
c = input()

for a in range(int(c)):
    total = 0
    count = 0
    n = list(map(int, input().split()))
    for i in range(1, len(n)):
        total = total + n[i]

    average = total / n[0]
    for j in range(1, len(n)):
        if n[j] > average:
            count += 1

    print('{0:.3f}%'.format(100 * count / n[0]))
