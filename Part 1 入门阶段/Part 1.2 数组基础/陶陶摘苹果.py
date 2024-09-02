apple_heights = list(map(int, input().split()))

taotao_height = int(input())

taotao_height_with_stool = taotao_height + 30

count = 0
for height in apple_heights:
    if height <= taotao_height_with_stool:
        count += 1

print(count)
