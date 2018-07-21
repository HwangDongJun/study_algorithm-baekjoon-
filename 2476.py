#주사위 게임
n = int(input())
nums = list()

for i in range(n):
    a, b, c = [int(x) for x in input().split()]
    if a == b and b == c and a == c:
        nums.append(10000 + a * 1000)
    elif a == b or b == c:
        nums.append(1000 + b * 100)
    elif a == c:
        nums.append(1000 + a * 100)
    else:
        nums.append(max([a, b, c]) * 100)

print(max(nums))
