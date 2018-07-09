#한수
# li[-1]은 배열의 마지막 원소에 해당 그냥 알아둘것
answer = 0
count = 0
n = int(input())
for i in range(1, n + 1):
    li = list(str(i))
    if len(li) > 2:
        gongcha = int(li[0]) - int(li[1])
        temp = gongcha
        for j in range(1, len(li)):
            if j != len(li)-1:
                gongcha = int(li[j]) - int(li[j+1])

                if temp == gongcha:
                    count += 1
    elif len(li) == 1:
        count += 1
    else:
        count += 1

print(count)