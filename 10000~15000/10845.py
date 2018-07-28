#큐
com = input()
data = list()

def switch(i):
    if i[0] == 'push':
        data.append(i[1])
    elif i[0] == 'pop':
        if len(data) == 0:
            print(-1)
        else:
            print(data.pop(0))
    elif i[0] == 'size':
        print(len(data))
    elif i[0] == 'empty':
        if len(data) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == 'front':
        if len(data) == 0:
            print(-1)
        else:
            print(data[0])
    elif i[0] == 'back':
        if len(data) == 0:
            print(-1)
        else:
            print(data[len(data) - 1])

for mand in range(int(com)):
    co = list(map(str, input().split()))
    switch(co)


