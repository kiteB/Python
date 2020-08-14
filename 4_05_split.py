# split
my_string = "1. 2. 3. 4. 5. 6"
print(my_string.split("."))
print(my_string.split(". "))

# Ex_1
full_name = "Kim, Yuna"
name_data = full_name.split(", ")
last_name = name_data[0]
first_name = name_data[1]

print(first_name, last_name)

# Ex_2 - 숫자들을 제외하고 모두 화이트 스페이스 존재
print("     \n\n    2   \t  3   \n  5 7 11  \n\n")
print("     \n\n    2   \t  3   \n  5 7 11  \n\n".split())

numbers = "     \n\n    2   \t  3   \n  5 7 11  \n\n".split()
print(numbers[0] + numbers[1])  # 숫자가 아닌 문자의 합!
print(int(numbers[0]) + int(numbers[1]))  # 정수로 형 변환!
