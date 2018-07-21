#모음의 개수
s = list(input())
mo = ['a', 'e', 'i', 'o', 'u']
count = 0

while s[0] != '#':
    for i in range(len(s)):
        for j in range(len(mo)):
            if s[i].lower() == mo[j]:
                count += 1
    print(count)
    count = 0
    s = list(input())