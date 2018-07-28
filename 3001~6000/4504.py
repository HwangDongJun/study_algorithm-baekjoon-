#배수 찾기
n = int(input())

a = int(input())
while(a != 0):
    if a % n == 0:
        print("{} is a multiple of {}.".format(a, n))
    else:
        print("{} is NOT a multiple of {}.".format(a, n))
    a = int(input())