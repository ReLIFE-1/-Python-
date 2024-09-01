n = int(input())
sign = 1 if n > 0 else -1
n = abs(n)
reversed_n = int(str(n)[::-1])
print(sign * reversed_n)
