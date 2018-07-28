#A+B -8
n = int(input())

for i in range(n):
    m = [int(x) for x in input().split()]
    print("Case #{}: {} + {} = {}".format(i+1, m[0], m[1], sum(m)))