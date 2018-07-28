#A+B -5
m = list(map(int, input().split()))
while m.count(0) != 2:
    print(sum(m))
    m = list(map(int, input().split()))