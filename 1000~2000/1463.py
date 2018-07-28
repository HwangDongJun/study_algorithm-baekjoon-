#1로 만들기
n = int(input())
check = 0
arraycheck = list()

def divthree(num, check):
    if num == 1:
        return arraycheck.append(check)
    #elif num % 3 != 0:
        #if num % 2 == 0:
            #divtwo(num, check)
        #minus(num, check)
    elif (num-1) % 2 == 0 or (num-1) % 3 == 0:
        minus(num, check)
    if num % 3 == 0 and num % 2 != 0:
        check += 1
        divthree(num/3, check)
    elif num % 2 == 0:
        check += 1
        divtwo(num/2, check)

def divtwo(num, check):
    if num == 1:
        return arraycheck.append(check)
    #elif num % 2 != 0:
        #if num % 3 == 0:
            #divthree(num, check)
        #minus(num, check)
    elif (num-1) % 2 == 0 or (num-1) % 3 == 0:
        minus(num, check)
    if num % 2 == 0 and num % 3 != 0:
        check += 1
        divtwo(num/2, check)
    elif num % 3 == 0:
        check += 1
        divthree(num/3, check)

def minus(num, check):
    if num == 1:
        return arraycheck.append(check)
    elif (num-1) % 2 == 0:
        check += 1
        divtwo(num-1, check)
    elif (num-1) % 3 == 0:
        check += 1
        divthree(num-1, check)

if n % 3 == 0:
    divthree(n, check)
    check = 0
if n % 2 == 0:
    divtwo(n, check)
    check = 0
if (n-1) % 2 == 0 or (n-1) % 3 == 0:
    minus(n, check)

print(min(arraycheck))
