#누울 자리를 찾아라
a = int(input())
one = list()
row_count = 0
col_count = 0
count = 0

for i in range(a):
    two = list(input())
    one.append(two)

perm = True
for j in range(a):
    ok_row = False
    if one[j].count('.') >= 2:
        for x in range(a):
            if one[j][x] == 'X':
                ok_row = False
                perm = True
            if one[j][x] == '.' and x+1 < a:
                if ok_row == False and perm:
                    ok_row = True
                else:
                    ok_row= False
                if one[j][x] == one[j][x+1]:
                    if ok_row:
                        row_count += 1
                        perm = False
                        continue

perm = True
for e in range(a):
    ok_col = False
    for k in range(a):
        if one[k][e] == 'X':
            ok_col = False
            perm = True
        if one[k][e] == '.' and  k+1 < a:
            if ok_col == False and perm:
                ok_col = True
            else:
                ok_col = False
            if one[k][e] == one[k+1][e]:
                if ok_col:
                    col_count += 1
                    perm = False
                    continue

print(row_count, col_count)