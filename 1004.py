#어린 왕자
import math as m

case = input()
co = 0

for i in range(int(case)):
    locone = list(map(int, input().split()))
    count = input()

    l = list()
    for j in range(int(count)):
        loctwo = list(map(int, input().split()))
        c = int(m.sqrt(m.pow(locone[0] - loctwo[0], 2) + m.pow(locone[1] - loctwo[1], 2)))
        d = int(m.sqrt(m.pow(locone[2] - loctwo[0], 2) + m.pow(locone[3] - loctwo[1], 2)))

        if loctwo[2] >= c and loctwo[2] <= d:
            co += 1
        if loctwo[2] >= d and loctwo[2] <= c:
            co += 1
        if loctwo[2] >= c and loctwo[2] >= d:
            co += 1

print(co)