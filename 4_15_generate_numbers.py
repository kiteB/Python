from random import randint


# 정답 숫자 3개를 뽑아줌.
def generate_numbers():
    numbers = []

    # 무작위로 0~9 사이의 서로 다른 숫자 3개를 뽑고,
    # 그 숫자들이 담긴 리스트 리턴
    while len(numbers) < 3:
        num = randint(0, 9)
        if num not in numbers:
            numbers.append(num)

    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers


# 출력
print(generate_numbers())


