#소수&팰린드롬
n = int(input())

while True:
    if n <= 2:
        print(2)
        break

    if n % 2 == 0:
        n += 1

    c = list(str(n))
    c.reverse()
    if n == int("".join(c)) and n != 1:
        ok = True
        for j in range(3, n, 2):
            if n % j == 0:
                ok = False
                break
        if ok:
            print(n)
            break
        else:
            n += 2
    else:
        n += 2