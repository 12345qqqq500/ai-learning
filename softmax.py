import math
scores = [1.0, 2.0, 3.0]

# 1. 每个数取 exp
# 2. 求和
# 3. 每个数除以总和
# 期望输出：[0.09, 0.245, 0.665]
# 提示：math.exp(s)、sum()、round(x, 3)。
exp_list = []
for s in scores:
    exp_list.append(math.exp(s))

print(exp_list)
total = sum(exp_list)
print(total)
result = []
for e in exp_list:
    result.append(round(e/total,3))
print(result)

