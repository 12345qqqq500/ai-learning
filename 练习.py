name = "张三"
age = 24
hourly = 2 #每天小时数
is_learning = True
print(f"{name}今年{age}岁，每天学{hourly}小时")
print(type(age), type(hourly), type(is_learning))
scores = [78, 92, 65, 88]
print(scores[0], scores[-1])     # 第一个、最后一个
scores.append(95)                # 加一个
print(len(scores), sum(scores) / len(scores))
print(scores[1:3])               # 切片：第2到第3个
week = {"周一": 2, "周二": 2, "周三": 0}
week["周四"] = 2
print(week["周一"])
print("周五" in week)            # 判断键在不在
for day, hours in week.items():
    print(day, hours)

