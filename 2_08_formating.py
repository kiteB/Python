# 오늘은 2020년 7월 21일입니다.
year = 2020
month = 10
day = 29

# print("오늘은 " + year + "년 " + month + "월" + day + "일입니다.") // Error
print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일입니다.")

# format 이용
print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))

# 더 간편하게
date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day))

# 다음날 출력

print(date_string.format(year, month, day + 1))
