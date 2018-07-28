#그대로 출력하기
while True:
    try:
        str = input()
        print(str)
    except EOFError:
        break