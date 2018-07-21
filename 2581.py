#소수
m = int(input())
n = int(input())
nums = list()

for i in range(m, n+1):
    if i == 2:
        nums.append(i)
    elif i != 1 and i % 2 != 0:
        ok = True
        for j in range(2, i):
            if i % j == 0:
                ok = False
                break
        if ok:
            nums.append(i)

if len(nums) == 0:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))