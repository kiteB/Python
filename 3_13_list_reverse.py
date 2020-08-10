numbers = [2, 3, 5, 7, 11, 13, 17, 19]

# 리스트 뒤집기
temp = []
for i in range(len(numbers)):
    temp.append(numbers[len(numbers) - i - 1])

for i in range(len(temp)):
    numbers[i] = temp[i]

print("뒤집어진 리스트: " + str(numbers))

# 모범 답안
for left in range(len(numbers) // 2):
    right = len(numbers) - left - 1     # 인덱스 left와 left와 대칭인 인덱스 right 계산
    numbers[right], numbers[left] = numbers[left], numbers[right]   # 위치 바꾸기

print("뒤집어진 리스트: " + str(numbers))