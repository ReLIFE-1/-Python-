l, m = map(int, input().split())
trees = [True] * (l + 1)

for _ in range(m):
    u, v = map(int, input().split())
    for i in range(u, v + 1):
        trees[i] = False

remaining_trees = sum(trees)
print(remaining_trees)