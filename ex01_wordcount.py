text = "这周学 Python，下周学 Python"

count = {}
for ch in text:
    if ch in " ，。":
        continue
    # TODO：让 count 里 ch 对应的数 +1
    count[ch] = count.get(ch, 0) + 1  #先别看，试着写
for ch, n in count.items():
    print(ch, n)