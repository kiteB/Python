my_family = {
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동민',
    '딸': '이지영'
}
# 사전의 겂 목록 출력
print(my_family.values())
print('이지영' in my_family.values())  # True
print('배연주' in my_family.values())  # False

# 목록으로 반복문을 돌고 싶을 때
for value in my_family.values():
    print(value)
# 사전의 키 목록 출력
print(my_family.keys())

# 응용 (사전에 있는 모든 값 출력)
for key in my_family.keys():
    value = my_family[key]
    print(key, value)

# 위의 코드보다 더 간단하게!
for key, value in my_family.items():
    print(key, value)
