#검증수
m = list(map(int, input().split()))

for i in range(len(m)):
    m[i] *= m[i]

print(sum(m) % 10)