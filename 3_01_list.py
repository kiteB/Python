# 리스트 (list)
numbers = [2, 3, 5, 7, 11, 13]
names = ["윤수", "혜린", "태호", "영훈"]

# 인덱싱 (indexing)
#print(numbers[6]) // Error 발생!
print(numbers[1] + numbers[3])

print(numbers[-6])  # numbers[0]
#print(numbers[-7]) // Error 발생!

# 리스트 슬라이싱 (list slicing)
print(numbers[0:4]) # 인덱스 0부터 4개!
print(numbers[2:])  # 인덱스 2부터 끝까지
print(numbers[:3])  # 처음부터 3개!

new_list = numbers[:3]  # [2, 3, 5]
print(new_list)

# 리스트 요소 바꾸기
numbers[0] = numbers[0] + numbers[1]
print(numbers)