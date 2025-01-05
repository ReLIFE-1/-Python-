n = int(input())
nums = list(map(int, input().split()))
count = 0
sums = set() # 集合不重复
for i in range(n):
    for j in range(i + 1, n):
        sums.add(nums[i] + nums[j])
for num in nums:
    if num in sums:
        count += 1
print(count)
