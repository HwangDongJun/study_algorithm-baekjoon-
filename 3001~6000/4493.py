#가위 바위 보?
n = int(input())

def game(one, two, p1, p2):
    if one == "R" and two == "P" or one == "S" and two == "R" or one == "P" and two == "S":
        p2 += 1
    elif one == "P" and two == "R" or one == "R" and two == "S" or one == "S" and two == "P":
        p1 += 1
    return p1, p2

for i in range(n):
    k = int(input())
    pone = 0
    ptwo = 0
    for j in range(k):
        a, b = [x for x in input().split()]
        pone, ptwo = game(a, b, pone, ptwo)

    if pone > ptwo:
        print("Player 1")
    elif pone < ptwo:
        print("Player 2")
    elif pone == ptwo:
        print("TIE")