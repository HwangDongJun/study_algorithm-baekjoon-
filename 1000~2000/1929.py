#소수 구하기
m, n = [int(x) for x in input().split()]
nums = list()

for i in range(m, n+1):
    if i == 2:
        nums.append(i)
    elif i != 1 and i % 2 != 0:
        ok = True
        for j in range(3, i, 2):
            if i % j == 0:
                ok = False
                break
        if ok:
            nums.append(i)

for a in range(len(nums)):
    print(nums[a])