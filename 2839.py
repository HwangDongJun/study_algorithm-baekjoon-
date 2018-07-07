#설탕 배달
sugar = int(input())
temp = 1002
answer = 1

for i in range(0, 1000):
    su = sugar - (5 * i)

    if su > 0:
        if su % 3 == 0:
            if temp > ((su // 3) + i):
                temp = (su // 3) + i
                answer = temp
        elif su % 5 == 0:
            if temp > ((su // 5) + i):
                temp = (su // 5) + i
                answer = temp
        elif sugar % 3 != 0 and sugar % 5 != 0 and answer != temp:
            answer = -1

print(int(answer))