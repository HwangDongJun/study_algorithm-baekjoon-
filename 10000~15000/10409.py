#서버
n, T = [int(x) for x in input().split()]
time = list(map(int, input().split()))

if len(time) == n:
    totaltime = 0
    count = 0
    for i in range(n):
        if count == i and totaltime+time[i] < T:
            totaltime += time[i]
            count += 1

    print(count)