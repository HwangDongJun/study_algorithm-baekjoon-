#나무 조각
m = list(map(str, input().split()))
n = m[:]
m.sort()

while n != m:
    temp = 0
    if n[0] > n[1]:
        temp = n[0]
        n[0] = n[1]
        n[1] = temp
        print(" ".join(n))
    if n[1] > n[2]:
        temp = n[1]
        n[1] = n[2]
        n[2] = temp
        print(" ".join(n))
    if n[2] > n[3]:
        temp = n[2]
        n[2] = n[3]
        n[3] = temp
        print(" ".join(n))
    if n[3] > n[4]:
        temp = n[3]
        n[3] = n[4]
        n[4] = temp
        print(" ".join(n))