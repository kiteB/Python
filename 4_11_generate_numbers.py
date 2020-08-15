from random import randint


def generate_numbers(n):
    # 무작위로 1~45 사이의 서로 다른 번호 n개를 뽑고,
    # 그 번호들이 담긴 리스트 리턴

    # 빈 리스트 생성
    numbers = []

    # 리스트의 개수가 n개가 되면 while 문 멈춤
    while len(numbers) < n:
        # 랜덤으로 1~45 사이의 서로 다른 번호 뽑기
        num = randint(1, 45)

        # num이 numbers에 없는 경우에만 추가하기
        if num not in numbers:
            numbers.append(num)

    # 리스트 반환
    return numbers


print(generate_numbers(6))