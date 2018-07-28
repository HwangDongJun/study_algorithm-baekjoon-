#알파벳 개수
temp = input()
s = list(temp)
a = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(s)):
    for j in range(97, 123):
        if int(ord(s[i])) == j:
            a[j-97] += 1

print(" ".join(map(str, a)))