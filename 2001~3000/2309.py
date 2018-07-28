#일곱 난쟁이
k = list()

for i in range(9):
    n = int(input())
    k.append(n)

num = sum(k) - 100
l = list()

for a in range(len(k)):
    if len(l) == 2:
        break
    for b in range(len(k)):
        if a == b or l.count(a) == 1 or l.count(b) == 1:
            continue
        elif k[a] + k[b] == num:
            l.append(a)
            l.append(b)
            break

l.sort()
k.remove(k[l[0]])
k.remove(k[l[1]-1])
k.sort()

for j in range(7):
    print(k[j])