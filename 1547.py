#공
n = int(input())
ball = [1, 0, 0, 0]

for i in range(n):
    m, n = [int(x) for x in input().split()]
    temp = ball[m-1]
    ball[m-1] = ball[n-1]
    ball[n-1] = temp

print(ball.index(1)+1)