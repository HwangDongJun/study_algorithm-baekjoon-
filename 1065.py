#한수
# li[-1]은 배열의 마지막 원소에 해당 그냥 알아둘것
answer = 0
ok = False
n = int(input())
for i in range(1, n + 1):
    li = list(str(i))
    if len(li) > 2:
        gongcha = int(li[0]) - int(li[1])
        temp = gongcha
        count = 2
        for j in range(1, len(li)):
            if j != len(li)-1:
                gongcha = int(li[j]) - int(li[j+1])

                if temp == gongcha:
                    count += 1
                    if count == len(li):
                        ok = True

        if ok and answer < i and i <= n:
            answer = i
            ok = False
    elif len(li) == 1:
        answer = i
    else:
        answer = i

print(answer)