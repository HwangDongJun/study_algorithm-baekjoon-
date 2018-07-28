#대소문자 바꾸기
str = list(input())
s = ""

for i in range(len(str)):
    if str[i].islower():
        s += str[i].upper()
    else:
        s += str[i].lower()

print(s)