from random import randint


def generate_numbers(n):
    # 무작위로 1~45 사이의 서로 다른 번호 n개를 뽑고,
    # 그 번호들이 담긴 리스트 리턴

    # 빈 리스트 생성
    numbers = []

    # 리스트의 개수가 n개가 되면 while 문 멈춤
    while len(numbers) < n:
        # 랜덤으로 1~45 사이의 서로 다른 번호 뽑기
        new_number = randint(1, 45)

        # num이 numbers에 없는 경우에만 추가하기
        if new_number not in numbers:
            numbers.append(new_number)


    # 리스트 반환
    return numbers

# 일반 당첨 번호 6개 + 보너스 번호 1개 리턴
def draw_winning_numbers():
    # 랜덤한 숫자 7개 생성
    winning_numbers = generate_numbers(7)
    # 일반 당첨 번호 6개는 정렬 & 보너스 번호는 그냥 추가!
    return sorted(winning_numbers[:6]) + winning_numbers[6:]


print(draw_winning_numbers())
