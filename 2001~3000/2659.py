#십자카드 문제
a, b, c, d = [x for x in input().split()]
num = list()

num.append(a+b+c+d)
num.append(b+c+d+a)
num.append(c+d+a+b)
num.append(d+a+b+c)
num.sort()

def check(s):
    c = list()
    result = list()
    for j in range(len(s)):
        n = list(str(s[j]))
        if n[0] == n[1] == n[2] == n[3]:
            c.append(int(n[0] + n[1] + n[2] + n[3]))
        else:
            c.append(int(n[0] + n[1] + n[2] + n[3]))
            c.append(int(n[1] + n[2] + n[3] + n[0]))
            c.append(int(n[2] + n[3] + n[0] + n[1]))
            c.append(int(n[3] + n[0] + n[1] + n[2]))
        c.sort()
        result.append(c[0])
        c.clear()

    return result

minnum = num[0]
num.clear()

for i in range(1111, int(minnum)):
    if str(i).count('0') == 0:
        num.append(i)

one = list()
count = 0
one = check(num)[:]
for a in range(len(num)):
    if one.count(num[a]) > 1:
        count = count + one.count(num[a]) - 1

print(len(num) + 1 - count)