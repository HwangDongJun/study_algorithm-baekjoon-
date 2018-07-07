#피보나치 함수
number = input()

def fibonacci(odi):
    lone = [1, 1]
    lzero = [1, 2]
    if odi == 0:
        print('1 0')
    elif odi == 1:
        print('0 1')
    elif odi == 2:
        print('1 1')
    else:
        for i in range(int(odi) - 3):
            lone.append(lone[i] + lone[i + 1])
            lzero.append(lzero[i] + lzero[i + 1])
        print('{} {}'.format(lone[len(lone) - 1], lzero[len(lzero) - 1]))


for a in range(int(number)):
    temp = input()
    fibonacci(int(temp))