nums = list(map(int, input().split()))
print(*nums[-2::-1]) # * 的作用是“解包”列表
