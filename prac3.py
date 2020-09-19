# 369 게임
# 3, 6, 9가 포함되어 있으면 '짝'
result = []

for i in range(1, 31):
    k = str(i)

    if k.find("3") > -1 or k.find("6") > -1 or k.find("9") > -1:
        print("박수치는 숫자 >>> ", i)
        result.append("짝")
    else:
        result.append(i)

print(result)