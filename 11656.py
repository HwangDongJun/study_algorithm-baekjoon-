#접미사 배열
s = list(input())
n = list()

for i in range(len(s)):
    input = "".join(s)
    n.append(input)
    s.pop(0)

for j in range(len(n)):
    print(sorted(n)[j])
