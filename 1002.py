import math

def distance(one, two, lengthone, three, four, lengthtwo):
    count = 0
    for a in range(0, 100):
        for b in range(0, 100):
            if float(lengthone) == math.sqrt(math.pow(one - a, 2) + math.pow(two - b, 2)) and float(lengthtwo) == math.sqrt(math.pow(three - a, 2) + math.pow(four - b, 2)):
                count += 1
    return count

inputnum = input()

for temp in range(int(inputnum)):
    li = list(map(int, input().split()))
    print(distance(li[0], li[1], li[2], li[3], li[4], li[5]))