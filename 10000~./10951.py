#A+B -4
while True:
    try:
        m = list(map(int, input().split()))
        print(sum(m))
    except EOFError:
        break