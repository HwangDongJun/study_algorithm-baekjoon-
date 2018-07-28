#ROT13
s = list(input())
password = list()

for a in range(78, 91):
    password.append(a)
for b in range(65, 78):
    password.append(b)

for i in range(len(s)):
    if s[i].isupper():
        s[i] = chr(password[ord(s[i]) - 65])
    elif s[i].islower():
        s[i] = chr(password[ord(s[i]) - 97] + 32)
    elif s[i].isspace() or s[i].isdigit():
        continue

print("".join(s))