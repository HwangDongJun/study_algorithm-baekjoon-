#나는 요리사다.
total = list()

for i in range(5):
    m = list(map(int,input().split()))
    total.append(sum(m))

print(total.index(max(total)) + 1, max(total))