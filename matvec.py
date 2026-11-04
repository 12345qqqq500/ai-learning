A = [[1, 2],
     [3, 4]]
x = [5, 6]
# 用两层 for 循环算出 A·x
# 期望输出：[17, 39]
result = []
""" for i in range(len(A)):
    row = A[i]        # 第 i 行，比如 [1, 2]
    # 这里将来放"算这一行的结果"
print("行数:", len(A)) """
for i in range(len(A)):
    row = A[i]
    total = 0
    for j in range(len(x)):
        total = total + row[j] * x[j]   #  这一行是核心
    # 现在 total 就是第 i 个结果
    print("第", i, "个结果:", total)
    result.append(total)
    print(result)