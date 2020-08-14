sum = 0
count = 0

with open('chicken.txt', 'r', encoding="UTF-8") as f:

    for line in f:
        # 자료 나누기
        day = line.split(": ")
        # 매출만
        sales = day[1]
        # 총 매출액 구하기
        sum += int(sales.strip())
        # 날짜 카운트
        count += 1

    print(sum/count)

