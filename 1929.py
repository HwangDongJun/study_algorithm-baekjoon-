#소수 구하기
m, n = input().split()

for i in range(int(m), int(n)+1):
    if i % 2 != 0:
        count = 1
        for j in range(2, i+1):
            if i % j == 0 and count <= 2:
                count += 1

        if count == 2:
            print(i)
