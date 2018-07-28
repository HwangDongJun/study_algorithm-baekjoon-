#막대기
bars = [64]
x = int(input())

def makebar(bars, x):
    bars.sort()
    if sum(bars) > x:
        temp = bars[0] / 2
        bars[bars.index(bars[0])] = temp

        if sum(bars) < x:
            bars.append(temp)

    if sum(bars) == x:
        print(len(bars))
    else:
        makebar(bars, x)

makebar(bars, x)