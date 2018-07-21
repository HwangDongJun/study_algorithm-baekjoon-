#단어의 개수
s = input().split(" ")
count = 0

for i in range(len(s)):
    if s[i] == '':
        count += 1

print(len(s) - count)