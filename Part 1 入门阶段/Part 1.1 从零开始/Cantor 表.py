def cantor(n):
    # 找到 n 所在的对角线
    diag = 1
    while n > diag:
        n -= diag
        diag += 1
    
    # 确定分子和分母
    if diag % 2 == 0:
        numerator = n
        denominator = diag - n + 1
    else:
        numerator = diag - n + 1
        denominator = n
    
    return f"{numerator}/{denominator}"

# 读取输入
N = int(input())

# 输出结果
print(cantor(N))



