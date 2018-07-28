#윷놀이
for i in range(3):
    m = list(map(int, input().split()))
    count = m.count(0)
    if count == 1:
        print('A')
    elif count == 2:
        print('B')
    elif count == 3:
        print('C')
    elif count == 4:
        print('D')
    else:
        print('E')
