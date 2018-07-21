#0 = not cute / 1 = cute
n = int(input())
check = [0, 0]

for i in range(n):
    p = int(input())
    if p == 0:
        check[0] += 1
    else:
        check[1] += 1

if check[0] > check[1]:
    print("Junhee is not cute!")
else:
    print("Junhee is cute!")