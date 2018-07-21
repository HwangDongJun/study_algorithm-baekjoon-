#알파벳 찾기
temp = input()
s = list(temp)
a = [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]

for i in range(len(s)):
    for j in range(97, 123):
        if ord(s[i]) == j and a[j-97] == -1:
            a[j-97] = i

print(" ".join(map(str, a)))