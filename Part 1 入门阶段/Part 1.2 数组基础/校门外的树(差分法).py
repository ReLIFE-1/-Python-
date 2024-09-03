l, m = map(int, input().split())
diff = [0] * (l + 2)
for i in range(m):
    u, v = map(int, input().split())
    diff[u] += 1
    diff[v + 1] -= 1

tree = 0
count = 0
for i in range(l + 1):
    count += diff[i]
    if count == 0:
        tree += 1

print(tree)