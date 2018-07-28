#유학 금지
str = list(input())
prohibition = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
removenum = list()

for i in range(len(str)):
    if prohibition.count(str[i]) == 1:
        removenum.append(i)

count = 0
for a in range(len(removenum)):
    if count == 0:
        str.remove(str[removenum[a]])
        count += 1
    else:
        str.remove(str[removenum[a] - count])
        count += 1

s = ""
for j in range(len(str)):
    s += str[j]

print(s)