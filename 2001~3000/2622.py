#삼각형만들기
num = int(input())
count = num + 1
result = 0

for a in range(1, count):
    for b in range(1, count):
        for c in range(1, count):
            if b > c and c > a:
                continue
            elif a+b+c == num and a < (b + c):
                result += 1

print(result)