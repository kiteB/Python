# 사전 (dictionary)
# key-value pair (키-값 쌍)
my_dictionary = {
    5: 25,  # key: 5, value: 25
    2: 4,
    3: 9
}
# 사전의 자료형 출력
print(type(my_dictionary))
# key가 3인 값의 value를 출력
print(my_dictionary[3])
# 사전에 변수 추가
my_dictionary[9] = 81
# 변수 추가 확인
print(my_dictionary)

# 사전은 정수가 아닌 다른 자료형도 추가 가능
my_family = {
    '엄마': '김자옥',
    '아빠': '이석진',
    '아들': '이동민',
    '딸': '이지영'
}
print(my_family['아빠'])