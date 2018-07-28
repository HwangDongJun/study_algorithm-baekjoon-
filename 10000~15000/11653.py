#소인수분해
n = int(input())
nums = [2]

for i in range(3, n+1):
    if i != 1 and i % 2 != 0:
        ok = True
        for j in range(3, i, 2):
            if i % j == 0:
                ok = False
                break
        if ok:
            nums.append(i)

def divnum(init, nlist, check=0):
    temp = nlist[check]
    if init % temp == 0:
        init /= temp
        print(temp)
        divnum(init, nlist, check)
    elif init != 1 and check != len(nlist)-1:
        check += 1
        divnum(init, nlist, check)

divnum(n, nums)
