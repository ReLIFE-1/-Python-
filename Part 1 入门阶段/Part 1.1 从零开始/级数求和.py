k = int(input())

sum = 0
n = 1
while sum <= k:
    sum += 1 / n
    n += 1

print(n - 1)