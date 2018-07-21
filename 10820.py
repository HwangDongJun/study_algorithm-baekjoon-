#문자열 분석
while True:
    try:
        n = list(input())
        check = [0, 0, 0, 0]

        for i in range(len(n)):
            if n[i].islower():
                check[0] += 1
            elif n[i].isupper():
                check[1] += 1
            elif n[i].isdigit():
                check[2] += 1
            elif n[i].isspace():
                check[3] += 1

        print(" ".join(map(str, check)))
    except EOFError:
        break