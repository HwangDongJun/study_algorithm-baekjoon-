#FBI
namelist = list()

for i in range(5):
    name = input()
    if name.count('FBI') == 1:
        namelist.append(str(i + 1))

if len(namelist) == 0:
    print("HE GOT AWAY!")
else:
    print(" ".join(namelist))