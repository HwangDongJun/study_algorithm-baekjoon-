number = input()
if not(int(number) <= 40 and int(number) >= 0):
    number = input()

def fibonacci(odi):
    fibo = [0, 0]
    if odi == 0:
        print('1 0')
    elif odi == 1:
        print('0 1')
    else:
        fibonacci(odi - 1) + fibonacci(odi - 2)

for a in range(int(number)):
    temp = input()
    fibonacci(int(temp))