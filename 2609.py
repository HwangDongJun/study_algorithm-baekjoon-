#최대공약수와 최소공배수
m = list(map(int, input().split()))

def makemax(nums, maxnum = 0):
    for i in range(1, min(nums)+1):
        if nums[0] % i == 0 and nums[1] % i == 0:
            if maxnum < i:
                maxnum = i

    return maxnum

def makemin(nums):
    num = makemax(nums)
    return int(abs((nums[0] * nums[1]) / num))

print(makemax(m))
print(makemin(m))