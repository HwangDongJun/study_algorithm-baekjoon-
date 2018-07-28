#세 수
numbers = list(map(int, input().split()))

max = max(numbers)
temp = 0
count = 0

for i in range(len(numbers)):
    if max > numbers[i]:
        if numbers[i] > temp:
            temp = numbers[i]
    if max == numbers[i] and count < 2:
        count += 1

if count == 2:
    print(max)
else:
    print(temp)