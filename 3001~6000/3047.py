#ABC
import statistics as st

m = list(map(int, input().split()))
str = input()

a = min(m)
b = st.median(m)
c = max(m)

if str == "ABC":
    print(a, b, c)
elif str == "ACB":
    print(a, c, b)
elif str == "BAC":
    print(b, a, c)
elif str == "BCA":
    print(b, c, a)
elif str == "CAB":
    print(c, a, b)
elif str == "CBA":
    print(c, b, a)