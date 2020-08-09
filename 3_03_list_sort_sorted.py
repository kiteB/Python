numbers = [19, 13, 2, 5, 3, 11, 7, 17]

# sorted
new_list = sorted(numbers)
print(new_list)
# 반대로 정렬
new_list = sorted(numbers, reverse=True)
print(new_list)

print("numbers:", numbers)
print()
# sort
# print(numbers.sort()) // None!
numbers.sort()
print(numbers)
# 반대로 정렬
numbers.sort(reverse=True)
print(numbers)