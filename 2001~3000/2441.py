#별찍기 -4
number = input()
arraystar = []
arrayspace = []
temp = ''
sp = ''
space = ' '
star = '*'

for i in range(0, int(number)):
    arrayspace.append(sp)
    temp = temp + star
    sp = sp + space
    arraystar.append(temp)

arraystar.reverse()
for j in range(len(arraystar)):
        answer = arrayspace[j] + arraystar[j]
        print(answer)
