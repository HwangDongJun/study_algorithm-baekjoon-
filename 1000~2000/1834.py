#나머지와 몫이 같은 수
n = int(input())

def checknum(n, str=list(), check=1):
    if n == 1:
        print(check+1)
        return False
    elif check == n * (n+1):
        print(sum(str))
        return False
    elif check // n == check % n:
        str.append(check)
    check += 1
    checknum(n, str, check)

checknum(n)
