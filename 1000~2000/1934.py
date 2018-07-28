#최소공배수
T = int(input())

def makemax(nums, maxnum = 0):
    for i in range(1, min(nums)+1):
        if nums[0] % i == 0 and nums[1] % i == 0:
            if maxnum < i:
                maxnum = i

    return maxnum

def makemin(nums):
    num = makemax(nums)
    return int(abs((nums[0] * nums[1]) / num))

for i in range(T):
    nums = list(map(int, input().split()))
    print(makemin(nums))