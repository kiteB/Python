from random import randint


# 무작위로 정답 번호 3개를 뽑는 함수
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


# 유저에게 번호 3개를 입력받는 함수
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")

    new_guess = []
    count = 1

    # 코드를 작성하세요.
    while len(new_guess) < 3:
        new_num = int(input("{}번째 숫자를 입력하세요: ".format(count)))

        if new_num < 0 or new_num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif new_num in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요")
        else:
            new_guess.append(new_num)
            count += 1

    return new_guess


# 유저 번호 3개와 정답 전호 3개를 비교해서, 스트라이크와 불 수 를 계산하는 함수
def get_score(guess, solution):     # guess = 유저가 뽑은 번호 3개가 담은 리스트
                                    # solution = 컴퓨터가 뽑은 정답 번호 3개가 담긴 리스트
    strike_count = 0    # 스트라이크 수
    ball_count = 0      # 볼 수

    # 숫자의 값과 위치가 모두 일치하면 스트라이크, 값만 맞으면 볼
    for i in range(3):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0

while True:

    guess = take_guess()
    s, b = get_score(guess, ANSWER)
    print("{}S {}B\n".format(s, b))
    tries += 1

    if s == 3:
        break
        
print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))