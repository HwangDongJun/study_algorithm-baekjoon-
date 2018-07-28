#시그마
m, n = [int(x) for x in input().split()]

print(int(((m + n) * (abs(n - m) + 1)) / 2))