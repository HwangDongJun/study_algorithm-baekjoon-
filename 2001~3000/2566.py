#최댓값
nums = list()

for i in range(9):
    n = list(map(int, input().split()))
    nums.append(n)

check = 0
one = 0
two = 0
for a in range(9):
    for b in range(9):
        if nums[a][b] > check:
            check = nums[a][b]
            one = a+1
            two = b+1

print(check)
print(one, two)


