max = 0
day = 0

for i in range(1,8):
    a,b = map(int,input().split())
    if a + b > 8:
        if a + b > max:
            max = a + b
            day = i

print(day)
    