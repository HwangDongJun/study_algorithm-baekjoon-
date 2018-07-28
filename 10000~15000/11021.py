#A+B -7
n = int(input())

for i in range(n):
    m = [int(x) for x in input().split()]
    print("Case #{}: {}".format(i+1, sum(m)))