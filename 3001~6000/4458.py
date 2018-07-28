#첫 글자를 대문자로
a = int(input())

for i in range(a):
    str = list(input())
    str[0] = str[0].upper()
    print("".join(str))
    str.clear()