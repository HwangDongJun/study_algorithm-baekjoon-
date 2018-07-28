#숫자의 합
temp = [0]
for i in range(2):
    m = list(map(int, input()))
    if temp[0] < sum(m):
        temp[0] = sum(m)

print(temp[0])