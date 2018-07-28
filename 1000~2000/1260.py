#DFS와 BFS
n, m, v = [int(x) for x in input().split()]
li = [[0 for x in range(n)] for y in range(n)]
for o in range(n):
    for t in range(n):
        li[o][t] = False

for i in range(m):
    a, b = [int(y)-1 for y in input().split()]
    li[a][b] = li[b][a] = True

dfs = list()
dfs.append(v)
for one in range(n):
    if len(dfs) != n:
        for two in range(n):
            if li[dfs[one]-1][two] == True and dfs.count(two+1) == 0:
                dfs.append(two+1)
                break
    else:
        break
bfs = list()
bfs.append(v)
for three in range(n):
    if len(bfs) != n:
        for four in range(n):
            if li[bfs[three]-1][four] == True and bfs.count(four+1) == 0:
                bfs.append(four+1)
    else:
        break

print(" ".join(map(str, dfs)))
print(" ".join(map(str, bfs)))
