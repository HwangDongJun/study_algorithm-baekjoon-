#정수 삼각형
n = int(input())
shape = []
total = []
check = n

for i in range(1, n+1):
    li = list(map(int, input().split()))
    shape.append(li)

def sum(form, check, num = 0):
    if check == 0:
        return num
    for i in range(0, len(form)):
        for j in range(len(form[i])):
            num += form[i][j]
            sum(form, check-1, num)

total.append(sum(shape, check))
print(total)