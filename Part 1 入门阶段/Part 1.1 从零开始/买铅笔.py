#买铅笔

n = int(input())

min_cost = float('inf')

for _ in range(3):
    pencils, price = map(int, input().split())
    packages = (n + pencils - 1) // pencils  # 向上取整
    total_cost = packages * price
    min_cost = min(min_cost, total_cost)

print(min_cost)
