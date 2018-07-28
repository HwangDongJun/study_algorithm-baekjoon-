#조세퍼스 문제
n, m = [int(x) for x in input().split()]
li = list()
sum = m - 1
result = list()

for i in range(1, n+1):
    li.append(i)

def checknum(temp, li):
    if temp < len(li):
        return temp
    temp -= len(li)
    return checknum(temp, li)

if n == 1:
    result.append(1)

m = m - 1
for j in range(0, n-1):
    result.append(li[m])
    if (len(li)-1) != 1:
        li.pop(m)
        if m >= len(li):
            m = 0

        m += sum
        m = checknum(m, li)
    else:
        li.pop(m)
        result.append(li[0])

print("<" + ", ".join(map(str, result)) + ">")