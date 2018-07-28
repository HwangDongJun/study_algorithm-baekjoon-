#터렛
import math

def distance(one, two, lengthone, three, four, lengthtwo):
    count = 0
    for a in range(-lengthone, lengthone):
        for b in range(-lengthtwo, lengthtwo):
            if float(lengthone) == math.sqrt(math.pow(one - a, 2) + math.pow(two - b, 2)) and float(lengthtwo) == math.sqrt(math.pow(three - a, 2) + math.pow(four - b, 2)):
                count += 1
    print(count)


inputnum = input()

for temp in range(int(inputnum)):
    li = list(map(int, input().split()))
    distance(li[0], li[1], li[2], li[3], li[4], li[5])