#점수 계산
scores = list()
checkscore = list()

for i in range(8):
    score = int(input())
    scores.append(score)
    checkscore.append(score)

sum = 0
index = list()
for j in range(5):
    m = max(scores)
    sum += m
    index.append(checkscore.index(m)+1)
    scores.remove(m)

print(sum)
index.sort()
print("{} {} {} {} {}".format(index[0], index[1], index[2], index[3], index[4]))