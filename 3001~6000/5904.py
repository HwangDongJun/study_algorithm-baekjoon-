#Moo 게임
t = int(input())
m = int(t // 5)

s = "moo"
str = "moo"
moo = list()

if m != 0:
    for j in range(m):
        moo += str
        for k in range(j+1):
            s += "o"
        moo += s
        moo += str
        str = moo[:]
        moo.clear()
        s = "moo"

print(str[t-1])
