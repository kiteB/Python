# 실수 -> 정수
print(int(3.8))

# 정수 -> 실수
print(float(3))

# 문자열 -> 숫자형
print(int("2") + int("5"))
print(float("1.1") + float("2.5"))

# 숫자형 -> 문자열
print(str(2) + str(5))

# Example
age = 7
# print("제 나이는 " + age + "살입니다.")   // Error!
print("제 나이는 " + str(age) + "살입니다.")  # 형 변환 필요

# Example
# print(int("Hello")) // "Hello"를 숫자로 바꿀 수 없기 때문!