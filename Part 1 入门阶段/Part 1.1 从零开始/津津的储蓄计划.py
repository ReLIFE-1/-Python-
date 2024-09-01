save = 0
money = 0

for month in range(1, 13):
    budget = int(input())
    money += 300  # 每月初收到300元

    if money < budget:
        print(-month)
        break

    left = money - budget
    save += left // 100 * 100
    money = left % 100

else:
    # 如果循环正常结束（没有break），计算最终金额
    total = money + int(save * 1.2)
    print(total)