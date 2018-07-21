#에디터
s = list(input())
cursor = len(s)
n = input()

for i in range(int(n)):
    command = input().split()

    if command[0] == 'L' and cursor != 0:
        cursor -= 1
    elif command[0] == 'D' and cursor != len(s):
        cursor += 1
    elif command[0] == 'B' and cursor != 0:
        cursor -= 1
        s.pop(cursor)
    elif command[0] == 'P':
        s.insert(cursor, command[1])
        cursor += 1

print("".join(s))